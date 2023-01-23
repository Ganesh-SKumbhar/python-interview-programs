# 18. Python program to convert float decimal to Octal number


def float_to_octal(num):

    whole, dec = map(int, str(num).split('.'))
    res = oct(whole).lstrip('0o')+'.'
    for x in range(3):
        if dec != 0:
            whole,dec = str((decimal_converter(dec))*8).split('.')
            dec = int(dec)
            res += whole
        else:
            return res+'0' # in case user enter int value return this
    return res

def decimal_converter(nm):
    while nm > 1:
        nm/=10
    return nm

num = float(input('Enter float number to get its octal: '))   # in case user enters int value

print(f'Octal conversion of {num} is :', float_to_octal(num))


# Enter float number to get its octal: 123.456
# Octal conversion of 123.456 is : 173.351
