# Returns the sum of digits in 2^n
def solution(n):
    num = pow(2,n)
    return sum_digits(num)

# Returns the sum of digits in a number
def sum_digits(n):
    digit_arr = [int(i) for i in str(n)]
    return sum(digit_arr)

print (solution(1000))
