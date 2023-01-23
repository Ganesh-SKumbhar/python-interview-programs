# 3. Python Program to find Factorial of Number
num = int(input('Enter number to find its factorial: '))
fact = 1
for i in range(1, num+1):
    fact = fact * i
print(f'Factorial of {num} is {fact}')

"""
Enter number to find its factorial: 4
Factorial of 4 is 24
"""
