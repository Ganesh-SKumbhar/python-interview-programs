# 5. Python Program to Check if binary representation is a palindrome
num = int(input('Enter a number : '))
bin_num = bin(num)[2:]  # skipping first 2 chars i.e. '0b'

if bin_num == bin_num[::-1]:
    print('Binary representation is palindrome ')
else:
    print('Binary representation is not palindrome ')

# Enter a number : 9
# Binary representation is palindrome 