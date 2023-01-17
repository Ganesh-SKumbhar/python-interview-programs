# 2. Python program to sort Python Dictionaries by Values

def sort_dict_by_values(dct1):
     return sorted(dct1.items(),key=lambda x:x[1])

print(sort_dict_by_values({'Three':9,'Six':36,'Two':4,'Eight':64,'Five':25}))


#o/p-
# [('Two', 4), ('Three', 9), ('Five', 25), ('Six', 36), ('Eight', 64)]