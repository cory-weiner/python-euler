twenty_map = {
    0:'',
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
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen'      
}
tens_map = {
    10:'ten',
    20:'twenty',
    30:'thirty',
    40:'forty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninety'
}

num_length_map = {
    1: 'hundred',
    2: 'thousand',
    3: 'milllion'
}

def get_num_string(num):
    places_arr = breakout_places(num)
    place_len = len(places_arr)
    word_str = ''
    for i,v in enumerate(places_arr):
        place = place_len - i
        word_str += three_digit_num_word(''.join(v))
        if place > 1:
            word_str += ' ' + num_length_map[place] + ' '
    return word_str


def breakout_places(n):
    numstring = str(n)
    str_arr = []
    while numstring:
        new_arr = [c for c in numstring[-3:]]
        str_arr.insert(0,new_arr)
        numstring = numstring[:-3]
    return str_arr



def three_digit_num_word(n):
    # Returns the word of a number up to three digits
    n = int(n)
    if n <= 19:
        return twenty_map[n]
    if n > 99:
        first_dig = int(str(n)[0])
        last_two_dig = str(n)[-2:]
        # if last_two_dig[0] == '0':
        #     tens_place = ''
        # else:
        if last_two_dig == '00':
            return twenty_map[first_dig] + ' hundred'
        if int(last_two_dig) <= 19:
            return twenty_map[first_dig] + ' hundred and ' + twenty_map[int(last_two_dig)]
        tens_place = tens_map[int(last_two_dig[0])*10]
        return twenty_map[first_dig] + ' hundred and ' + tens_place + twenty_map[int(last_two_dig[1])]
    return tens_map[int(str(n)[0])*10] + twenty_map[int(str(n)[1])]

def solution(n):
    solution_arr = []
    for i in range(1,n+1):
        solution_arr.append(get_num_string(i).replace(' ',''))
    i = 0
    for v in solution_arr:
        i+= len(v)
    return i

print(solution(1000))