# 9. Python Program to Find the minimum sum of factors of a number
def min_sum_factors(num):
    factor_sum = 0
    while num>0:
        for i in range(2,num):
            if num%i == 0:
                factor_sum += i
                num = num // i
                break
        else:
            factor_sum += num
            num //= num
            break
    return factor_sum

num = int(input('enter number : '))
print('Minimum sum of factors is : ', min_sum_factors(num))

# enter number : 105
# Minimum sum of factors is :  15