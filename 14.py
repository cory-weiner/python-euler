def solution(n):
    max_n = 1
    max_sn = 1
    while n > 0:
        print(n)
        chain = collatz_chain([n])
        t = collatz_chain(chain)
        if len(chain) > max_n:
            max_n = len(chain)
            max_sn = n
        n-= 1
    return max_sn



def collatz_chain(chain): 
    n = chain[-1]
    if n == 1:
        return chain
    if n % 2 == 0:
        chain.append(n/2)
    else:
        chain.append((3*n) + 1)
    return collatz_chain(chain)

print (solution(1000000))
