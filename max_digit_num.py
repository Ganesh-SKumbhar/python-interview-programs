# 11. Python Program for Largest and Smallest K digit number divisible by X

K = int(input('Digits: '))
X = int(input('Divisible by : '))

min_Kdigit_num = pow(10, K - 1)

if min_Kdigit_num % X == 0:
    print(f"Smallest {K} digit number divisible by {X} : ", min_Kdigit_num)
else:
    print(f"Smallest {K} digit number divisible by {X} : ", (min_Kdigit_num + X) - ((min_Kdigit_num + X) % X))

# --------------------------------------------------------------------
max_Kdigit_num = pow(10, K) - 1
print(max_Kdigit_num)

if max_Kdigit_num % X == 0:
    print(f"Largest {K} digit number divisible by {X} : ", max_Kdigit_num)
else:

    print(f"Largest {K} digit number divisible by {X} : ", (max_Kdigit_num - (max_Kdigit_num + X) % X))


# Digits: 5
# Divisible by : 87
# Smallest 5 digit number divisible by 87 :  10005
# 99999
# Largest 5 digit number divisible by 87 :  99963