twenty_map = {
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixten',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen'      
}
tens_map = {
    20:'twenty',
    30:'thirty',
    40:'forty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninety'
}


def solution(n):
    num_length = math.ceil(len(str(num))/3)
    num_length_map = {
        1: 'hundred',
        2: 'thousand',
        3: 'milllion'
    }

def two_digit_num_word(n):
    if n <= 19:
        return twenty_map[n]
    return tens_map[int(str(n)[0])*10] + twenty_map[int(str(n)[1])]
        

print(solution(999))