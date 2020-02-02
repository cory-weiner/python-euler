def solution():
    results = set()
    for i in range(1,99):
        if i < 10:
            s = 1234
        if i > 10:
            s = 123
        for r in range(s,10000//i):
            product = i * r
            num_string = str(i) + str(r) + str(product)
            if is_pandigital(num_string):
                results.add(product)
    return results




def is_pandigital(n):
    digits = [int(i) for i in str(n)]
    for i in range(1,len(digits)+1):
        if i not in digits:
            return False
    return True

sol = solution()
print(sol)
print(sum(sol))

# def printAllKLengthRec(set, prefix, n, k): 
#     if (k == 0) : 
#         print(prefix) 
#         return
#     for i in range(n):  
#         newPrefix = prefix + set[i] 
#         printAllKLengthRec(set, newPrefix, n, k - 1) 


# set = ['1','2','3','4','5','6','7','8','9']
# n = len(set)
# printAllKLengthRec(set, "", n, 3) 


# print(solution(1000))

# set = {'1','2','3','4','5','6','7','8','9'}

# get_permutes_of_size(['1','2','3','4'],2)