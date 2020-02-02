# How do we define max_n on this problem?
# testing all nums up to 10000000 yields correct result
def sum_of_pow(n,topow):
    if sum([pow(int(i),topow) for i in str(n)]) == n: return True
    return False

def solution(max_n,topow):
    passes_test = []
    for i in range(2,max_n):
        if sum_of_pow(i,topow): passes_test.append(i)
    return sum(passes_test)



print(solution(10000000,5))