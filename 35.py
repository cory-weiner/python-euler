import math
from itertools import permutations

def get_primes(n):
    # Returns array of all prime numbers up to n
    # Uses Sieve of Eratosthenes to eliminate composite numbers
    n = n+1 # to make list inclusive 
    prime_map = [1]*n
    prime_map[0]=0
    prime_map[1]=0
    for i in range(2,int(math.sqrt(n))):
        if prime_map[i]==0:
            i+=1
            continue
        j = 2*i
        while j < n:
            prime_map[j] = 0
            j+=i
    return dict.fromkeys([i for i,v in enumerate(prime_map) if v == 1])

# def get_permutations(n):
#     return [int(''.join(p)) for p in permutations(str(n))] 

def get_rotations(n):
    n_str = str(n)
    return [int(n_str[i:]+n_str[:i]) for i,v in enumerate(n_str)]


def solution(n):
    primes = get_primes(n)
    circulars = []
    for p in primes:
        if p == 1193:
            print('break')
        satisfies = True
        for perm in get_rotations(p):
            if perm not in primes:
                satisfies = False
                break
        if satisfies: 
            circulars.append(p)
    return circulars
            
print(len(solution(1000000)))

             
