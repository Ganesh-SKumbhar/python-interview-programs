# 5. Python program to merge two Dictionaries

dct1 = {'A':'Alpha', 'B': 'Beta', 'D': 'Delta'}
dct2 = {'D':'Delta', 'L':'Lambda', 'P': 'Pi'}

def merge_dict(dct1,dct2):
    dct1.update(dct2)
    return dct1

print('Merged Dictionaries : ', merge_dict(dct1, dct2))


#o/p- Merged Dictionaries :  {'A': 'Alpha', 'B': 'Beta', 'D': 'Delta', 'L': 'Lambda', 'P': 'Pi'}

