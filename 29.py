def solution():
    # A vals:
    result = set()
    for a in range(2,101):
        for b in range(2,101):
            result.add(pow(a,b))
    return result

print(len(solution()))