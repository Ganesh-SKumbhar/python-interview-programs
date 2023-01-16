# 16. Python Program to Find the sum of even factors of a number

def sum_of_even_factors(num):
    sum_of_even = 0
    while num > 0:
        for i in range(2,num):
            if num%i == 0:
                if i%2 == 0:
                    sum_of_even += i
                num //= i
                break
        else:
            break

    return sum_of_even

num = int(input('enter number : '))
print(f'Sum of even factors of {num} is : {sum_of_even_factors(num)}')


# enter number : 100
# Sum of even factors of 100 is : 4
