def solution(max):
    fib_numbers = [1,2]
    even_sum = 2
    i = 2
    while True:
        new_num = sum(fib_numbers[i-2:i])
        i+=1
        if new_num > max:
            break
        fib_numbers.append(new_num)
        if new_num%2 == 0:
            even_sum += new_num
    print(fib_numbers)
    return even_sum
    

print(solution(400000))