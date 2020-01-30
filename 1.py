def solution(max):
    valid_values = []
    for i in range(0,max):
        if i%3 == 0 or i%5 == 0:
            valid_values.append(i)
    return sum(valid_values)

print(solution(1000))