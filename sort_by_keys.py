# 1. Python program to sort Python Dictionaries by Keys

def sort_dict_by_keys(dct):
    return sorted(dct.items())

print(sort_dict_by_keys({'Three':9,'Six':36,'Two':4,'Eight':64,'Five':25}))

#o/p-
#  [('Eight', 64), ('Five', 25), ('Six', 36), ('Three', 9), ('Two', 4)]