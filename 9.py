import math
def solution(target_sum):
    a = target_sum
    while a >=1:
        b = 1
        while b < a:
            c = math.sqrt(pow(a,2) + pow(b,2))
            if a + b + c == target_sum:
                return product_of_arr([a,b,c])
            b += 1
        a -= 1
    
            
def product_of_arr(arr):
    result = 1
    for i in arr:
        result *= i
    return result

        
    

print(solution(1000))