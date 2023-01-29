# 7. Print anagrams together in Python using List and Dictionary
list1= ['bag', 'bat', 'tab', 'gab']

def anagrams(lst):
    dct = {}
    for ele in lst:
        item = ''.join(sorted(ele))
        if item in dct:
            dct[item].append(ele)
        else:
            dct[item] = [ele]
    return list(dct.values())

print('List of anagrams: ', anagrams(list1))


# o/p- List of anagrams:  [['bag', 'gab'], ['bat', 'tab']]