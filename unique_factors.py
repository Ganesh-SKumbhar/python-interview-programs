# 2. Python Program for Product of unique prime factors of a number

from functools import reduce

num = int(input())
factor_list = []
while num > 0:
    for divisor in range(2, (num // 2) + 1):
        if num % divisor == 0:
            factor_list.append(divisor)
            num = num // divisor
            break
        else:
            continue
    else:
        factor_list.append(num)
        num = num // num
        break
unique_factors = set(factor_list)
product = 1
print('product of unique factors is : ',reduce(lambda x,y:x*y, unique_factors))

"""  o/p-- 
100
product of unique factors is :  10

"""