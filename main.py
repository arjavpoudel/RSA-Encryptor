import random
random.seed(14)

#intializes 2 random prime numbers, stores their product as N and their totient as phi_N
p = 23
q = 31
N = p*q
phi_N = (p-1) * (q-1)


#returns Greatest Common Divisor between p and q
def GCD(p,q):
    while q!= 0:
        p, q = q, p%q
    return p

'''
takes two integers p and q as input, and returns p if it is coprime to q (i.e., if their GCD is 1). 
If p is equal to 1 or not coprime to q, then the function returns nothing
'''
def get_coprime(p,q):
    if p ==1:
        pass
    elif GCD(p,q) == 1:
        return p
    else:
        pass

    
'''
For each number e, the get_coprime function is called with parameters e and N, 
and the result is appended to the public_key_0 list.
'''

coprime_list = [e for e in range(1, phi_N) if GCD(e, N) == 1 and GCD(e, phi_N) == 1]
public_key_candidates = [e for e in coprime_list if get_coprime(e, phi_N) in coprime_list]

E = random.choice(public_key_candidates)
print(f"E is: {E}")

private_key_candidates = [D for D in range(1,N) if (E*D) % phi_N ==1]

D = random.choice(private_key_candidates)
print(f"D is: {D}")

print(f"the public key is {E,N}")


while True:
    message = int(input(f"Pick a number less than {N}: "))
    if message >= N:
        print()
        print(f"Warning: Number outwith range. Please try again.")
    else:
        break

encrypt  = (message**E)%N

print(f"The encrypted message is: {encrypt}")

decrypt= (encrypt**D)%N
print(f"Your original message was: {decrypt}")


