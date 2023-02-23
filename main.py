import random
from helper_functions import get_prime_candidates, get_private_key, is_prime, get_coprime, wordToNum


def main():
    # Generate two random prime numbers
    p_candidates = get_prime_candidates(2, pow(10,4))
    p = random.choice(p_candidates)
    q_candidates = [q for q in p_candidates if q != p]
    q = random.choice(q_candidates)
    #print(f"p is: {p}")
    #print(f"q is: {q}")

    # Compute N and phi_N
    N = p * q
    phi_N = (p - 1) * (q - 1)

    # Generate the public key
    E = get_coprime(phi_N, N)
    #print(f"E is: {E}")
    public_key = (E, N)
    print(f"public key: {public_key}")

    # Generate the private key
    D = get_private_key(E, phi_N)
    #print(f"D is: {D}")
    private_key = (D, N)
    print(f"private key: {private_key}")

    # Encrypt and decrypt a message
    raw_message = input("Enter your message here: ")
    integer_message = wordToNum(raw_message)
    print(f"integer message: {integer_message}")
    encrypted = hex(pow(integer_message, E, N))
    print(f"encrypted message: {encrypted}")

    d_test = int(input("enter first index val of private key to decrypt: "))

    decrypted = pow(int(encrypted,16), d_test, N)
    print(f"decrypted integer message: {decrypted}")
    if decrypted == integer_message:
        print("success!")
        print(f"original message: {raw_message}")
        
    else:
        print("decryption unsuccessful.")

if __name__ == '__main__':
    main()
