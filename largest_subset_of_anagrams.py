# 9. Python Counter to find the size of the largest subset of anagram words

list1 = ['bag', 'bat', 'tab', 'gab', 'tba']


def anagrams(lst):
    dct = {}
    for ele in lst:
        item = ''.join(sorted(ele))
        if item in dct:
            dct[item].append(ele)
        else:
            dct[item] = [ele]

    return list(sorted(dct.values())[-1])


print('size of the largest subset of anagram words: ', len(anagrams(list1)))

# o/p- size of the largest subset of anagram words:  3
