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
coprime_list_0 = range(1,phi_N)
public_key_0 = []
for e in coprime_list_0:
        public_key_0.append(get_coprime(e,N))

coprime_list_1 = range(1,phi_N)
public_key_1 = []
for e in coprime_list_1:
        public_key_1.append(get_coprime(e,phi_N))



public_key_2 =[]
for elem in public_key_1:
    if elem in public_key_0:
        public_key_2.append(elem)


e_candidates =[]
for elem in public_key_2:
    if elem != None:
        e_candidates.append(elem)

E = random.choice(e_candidates)
print(f"E is: {E}")

private_key_0 = range(1,N)
private_key_1 = []
for D in private_key_0:
    if E*D % phi_N == 1:
       private_key_1.append(D)
D = random.choice(private_key_1)


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


