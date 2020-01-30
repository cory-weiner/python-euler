# Use a nested loop to iterate through the list, checking if each value is a palindrome
# Once a palindrome is found, we know the lower bound for the second list is the max value from the first iteration
# The upper bound is the decrementing number.

def is_palendrome(num):
    numstring = str(num)
    return(numstring == numstring[::-1])

def solution():

    n = 999
    maxv = 0
    lower_bound = 1
    while n >= 100:
        i = n
        while i >= lower_bound:
            if(is_palendrome(i * n)):
                maxv = max(maxv,i*n)
                lower_bound = i
                break
            i-=1
        n-=1
    return maxv


print(solution())