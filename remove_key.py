# 4. Python program to remove a key from a dictionary

def remove_key(dct,key):
    if key in dct:
        dct.pop(key)
        return 'list after deleting key : ', dct
    else:
        return 'No such key present'

dct = {'Three':9,'Six':36,'Two':4,'Eight':64,'Five':25}
print('Dictionary is :', dct)
print(remove_key(dct,input('Enter the key you want to remove: ').capitalize()))


#o/-p-
#Dictionary is : {'Three': 9, 'Six': 36, 'Two': 4, 'Eight': 64, 'Five': 25}
#Enter the key you want to remove: one
#No such key present