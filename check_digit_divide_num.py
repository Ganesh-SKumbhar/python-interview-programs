# 17. Python Program to Check if all digits of a number divide it

def check_if_all_digits_divide_num(num):
    temp = num

    while temp > 0:
        if temp % 10 == 0:
            return 'No'
        else:
            last_digit = temp % 10
            if num%last_digit == 0:
                temp //= 10
                continue
            else:
                return 'No'
    return'Yes'


num = int(input('enter number : '))
print(f'All digits of a number {num}  divides it ? : {check_if_all_digits_divide_num(num)}')


# enter number : 1244
# All digits of a number 1244  divides it ? : Yes
