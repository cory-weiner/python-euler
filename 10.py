import math
import numpy as np
def solution(maxv):
    primes = [2.0]
    n = 3
    while n < maxv:
        if is_prime(n): primes.append(n)
        n+=2.0
    return np.sum(primes, dtype=np.int64)


def is_prime(n):
    max_n = math.sqrt(n)
    i = 2
    while i <= max_n:
        if n % i == 0:
            return False
        i+=1
    return True
    


print(solution(2000000))