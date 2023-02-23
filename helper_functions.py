import random


#checks whther a number in a given range is prime or not
is_prime = lambda n: n >= 2 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))


#Generates a list of prime candidates between start and end.
get_prime_candidates = lambda start, end: [p for p in range(start, end) if is_prime(p)]

def get_coprime(phi_N, N):
    """
    Generate a random coprime of phi_N and N.
    """
    while True:
        e = random.randint(2, phi_N - 1)
        if is_prime(e) and (e != N) and (phi_N % e != 0):
            return e


get_private_key = lambda E, phi_N: random.choice([D for D in range(1, phi_N) if (E*D) % phi_N == 1])


def wordToNum(string):
    ords = [ord(q) for q in list(string)]
    sum = 0 
    for num in ords:
        sum+=num
    return sum

