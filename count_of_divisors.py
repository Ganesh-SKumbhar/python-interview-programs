# 8. Python Program to Check if a count of divisors is even or odd
def count_of_divisors(num):
    divisors = 0
    for i in range(1,(num//2)+1):
        if num%i == 0:
            divisors += 1
    print(divisors)
    if divisors%2 == 0:
        return 'Even'
    else:
        return 'Odd'

num = int(input('enter number : '))
print('Count of divisor is : ', count_of_divisors(num))

# enter number : 20
# 5
# Count of divisor is :  Odd