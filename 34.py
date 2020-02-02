# We can likely define an upper limit, but I have hardcoded at 999999
import math
def factorial_sum(n):
    return sum([math.factorial(int(i)) for i in str(n)])

def solution():
    result = []
    for i in range(10,999999):
        if i == factorial_sum(i):
            result.append(i)
    return sum(result)

print(solution())
    