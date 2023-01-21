# 15. Python program to find the most occurring character and its count
from collections import Counter
from functools import reduce

str1 = input("Enter any string: ")
dic = Counter(str1)
most_occur_char = max(dic.values()) # max value
max_ele = max(dic,key=dic.get)

print(f'Maximum occuring character is: "{max_ele}" which is occured :- {most_occur_char} times')

# Enter any string: ganeshkumbharpython
# Maximum occuring character is: "h" which is occured :- 3 times

