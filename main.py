import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                   'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
characters = []
output, try_as_int, make_char_list, use_num, use_caps, all_caps, only_num = '', True, True, True, False, False, False

print('Enter length of desired string (or string of equivalent length)\nType \"exit\" to end program')
while True:
    word_length = input('Input: ')
    if word_length.startswith(' '):
        for i, char in enumerate(word_length):
            if char != ' ':
                word_length = word_length[i:]
                break
    if word_length == 'exit':
        break
    if word_length == 'help':
        print('-c or -caps: include capital letters\n-ac or -allcaps: exclude lowercase letters')
        print('-nn or -nonum: do not include numbers\n-on or -onlynum: use only numbers')
        print('press RETURN on blank input to repeat generation')
        continue
    if word_length == '' and output != '':
        word_length, make_char_list = output, False
    elif word_length.startswith('-') and output != '':
        word_length = ''.join([output, ' ', word_length])
        make_char_list, use_num, use_caps, all_caps, only_num = True, True, False, False, False
    else:
        try_as_int, make_char_list, use_num, use_caps, all_caps, only_num = True, True, True, False, False, False
    if ' -' in word_length:
        if ' -c' in word_length or ' -caps' in word_length:
            use_caps = True
        if ' -ac' in word_length or ' -allcaps' in word_length:
            use_caps, all_caps = True, True
        if ' -nn' in word_length or ' -nonum' in word_length:
            use_num = False
        if ' -on' in word_length or ' -onlynum' in word_length:
            only_num = True
        for i, char in enumerate(word_length):
            if char == '-' and word_length[i - 1] == ' ':
                word_length = word_length[:i - 1]
                break
    try:
        if try_as_int:
            word_length = int(word_length)
        else:
            raise ValueError
    except ValueError:
        word_length = len(word_length)
        try_as_int = False
    if make_char_list:
        characters = []
        if not all_caps and not only_num:
            characters.extend(letters)
        if use_caps and not only_num:
            characters.extend(capital_letters)
        if use_num:
            characters.extend(numbers)
    if not characters:
        print('(ಠ_ಠ)?')
        continue
    print(output := ''.join([characters[random.randint(0, len(characters) - 1)] for _ in range(word_length)]))
