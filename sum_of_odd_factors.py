# 4. Python Program for Find sum of odd factors of a number
num = int(input('Enter any number : '))
factors = []
for i in range(1, (num//2)+1):
    if num % i == 0:
        factors.append(i)
print(f'Factors of {num} are : {factors} ')
print('Sum of odd factors: ', sum([i for i in factors if i % 2 != 0]))

"""  o/p-- 
Enter any number : 50
Factors of 50 are : [1, 2, 5, 10, 25] 
Sum of odd factors:  31
"""