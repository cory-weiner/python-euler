from decimal import *
getcontext().prec = 2500

# Solution is inefficient, but checks for recurring sequence, breaking if a consecutive 3 characters are in the number.
def solution(n):
    all_seq = {}
    max_d = 0
    max_seq = []
    for i in range(2,n):
        dec_str = str(Decimal(1)/i)[2:]
        sequence = [dec_str[0]]
        if len(dec_str) < 999:
            continue
        for index,char in enumerate(dec_str[1:]):
            if sequence[-1:][0] == char and dec_str[i+1] == char and dec_str[i+2] == char:
                sequence = [char]
                all_seq[i] = sequence
                break
            compare_seq = list(dec_str[index+1:index+1+len(sequence)])  
            if sequence == compare_seq and len(compare_seq)>1:
                if len(sequence) > len(max_seq):
                    max_d = i
                    max_seq = sequence
                all_seq[i] = sequence
                break
            else:
                sequence.append(char)
    return {'max_seq': max_seq, 'max_d': max_d}

print(solution(1000))
