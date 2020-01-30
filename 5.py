
def solution(n):
    result = n*2
    while True:
        for i in range(2,n+1):
            if result % i != 0:
                result += n
                break
            if i == n:
                return result

print(solution(20))