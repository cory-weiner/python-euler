import math
def solution(n):
    return(sum_digits(math.factorial(n)))


def sum_digits(n):
    digit_arr = [int(i) for i in str(n)]
    return sum(digit_arr)

print(solution(100))