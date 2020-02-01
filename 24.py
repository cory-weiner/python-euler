from itertools import permutations

def solution(word):
    per = [''.join(p) for p in permutations(word)]
    per.sort()
    return per[999999]

print(solution('0123456789'))

