def solution(data):
    total = 0
    for index,word in enumerate(data):
        total += (index+1) * word_score(word)
    return total

def word_score(w):
    charmap = {
        'A':1,
        'B':2,
        'C':3,
        'D':4,
        'E':5,
        'F':6,
        'G':7,
        'H':8,
        'I':9,
        'J':10,
        'K':11,
        'L':12,
        'M':13,
        'N':14,
        'O':15,
        'P':16,
        'Q':17,
        'R':18,
        'S':19,
        'T':20,
        'U':21,
        'V':22,
        'W':23,
        'X':24,
        'Y':25,
        'Z':26
    }
    score = 0
    for char in w:
        score+= charmap[char]
    return score
import os
path = os.getcwd() + '\python-euler\p022_names.txt'
print(path)
data = open(path,'r').read().split(',')
data = [name[1:-1] for name in data]
data.sort()

print(solution(data))
