# 20. Write a Python program to replace whitespaces with an underscore and vice versa
str1 = input()
replacement = ''.maketrans(' -','- ')
str1.translate(replacement)


# he is very-very nice
# 'he-is-very very-nice'

# ------------------------------------------------------------------------------------------------------------------

# 22. Write a Python program to find all words starting with 'a' or 'e' in a given string.
str1 = input('Enter string: ')

print("Words starting with 'a' or 'e' : ", [i for i in str1.split() if i.startswith('a') or i.startswith('e')])

# Enter string: python is easy to learn and easy to read
# Words starting with 'a' or 'e' :  ['easy', 'and', 'easy']

# ------------------------------------------------------------------------------------------------------------------

# 23. Write a Python program to abbreviate 'Road' as 'Rd.' in a given string.
str1 = input('Enter string: ')
print('Abbreviation is: ',str1[0].upper()+str1[-1]+'.')

# Enter string: road
# Abbreviation is:  Rd.

