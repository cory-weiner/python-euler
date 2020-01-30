
def solution(n):
    sum_of_squares = sum([i*i for i in range(1,n+1)])
    square_of_sum = pow(sum([i for i in range(1,n+1)]),2)
    return square_of_sum - sum_of_squares

print(solution(100))