# 10. Python Dictionary to find mirror characters in a string

def mirror_chars(str1):
    begin = 'abcdefghijklmnopqrstuvwxyz'
    end = 'zyxwvutsrqponmlkjihgfedcba'

    mirror_dct = dict(zip(begin, end))  # dictionary of mirror letters
    mirror_str = ''
    for letter in str1:
        mirror_str += mirror_dct[letter]
    return mirror_str


print('Mirror character of string :', mirror_chars(input('Enter any string: ')))


#o/p-  Enter any string: ganesh
# Mirror character of string : tzmvhs
