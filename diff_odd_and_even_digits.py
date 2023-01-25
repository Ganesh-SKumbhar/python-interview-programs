# 10. Python Program to find Difference between sums of odd and even digits

def difference_of_odd_and_even_digits(num):
    odd_dig_sum = 0
    even_dig_sum = 0

    while num > 0:
        dig = num % 10
        num = num // 10
        if dig % 2 == 0:
            even_dig_sum += dig
        else:
            odd_dig_sum += dig

    return abs(odd_dig_sum - even_dig_sum)


num = int(input('enter number : '))
print('Difference between sums of odd and even digits is : ', difference_of_odd_and_even_digits(num))

# enter number : 123456
# Difference between sums of odd and even digits is :  3