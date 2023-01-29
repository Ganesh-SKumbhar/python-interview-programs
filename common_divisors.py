# 7. Python Program for Common Divisors of Two Numbers
def common_divisors(num1,num2):
    min_num = min(num1,num2)
    common_div = []
    for i in range(1,min_num+1):
        if num1%i == 0 and num2%i == 0:
            common_div.append(i)
    return common_div

num1,num2 = map(int,input('Enter two numbers space separated:  ').split())
print('Common divisors of two numbers are : ', common_divisors(num1,num2))

# Enter two numbers space separated:  16 64
# Common divisors of two numbers are :  [1, 2, 4, 8, 16]