import math

def solution(n):
    primes = [2]
    inc = 3
    while len(primes) < n:
        if is_prime(inc): primes.append(inc)
        inc +=2
    return primes[n-1]


def is_prime(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

print(solution(10001))