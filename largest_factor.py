# 1. Python Program for Find largest prime factor of a number

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
print(factor_list, ' largest factor is :', max(factor_list))

"""  o/p--
24
[2, 2, 2, 3]  largest factor is : 3
"""