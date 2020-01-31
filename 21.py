def solution(n):
    # This could be improved by not recalculating all the relational divisor sums
    # Instead maintain a map of all calculated sums and check against the map.
    dsum_map = {}
    for i in range(2,n):
        dsum_map[i] = sum_divisors(i)
    result = []
    for key,value in dsum_map.items():
        amic_check = sum_divisors(value)
        if amic_check == key and amic_check < n and key < n and value != amic_check:
            result.append(key)        
    return sum(result)


def sum_divisors(n):
    divisor_sum = 1
    for i in range(2,n):
        if n % i == 0 : 
            divisor_sum += i
    return divisor_sum

print(solution(10000))    