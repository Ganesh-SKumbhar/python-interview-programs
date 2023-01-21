# 12. Python program to convert a list of Tuples into Dictionary
lst_tuple = [(12, 45), (31, 23), (67, 55), (43, 84), (98, 32)]


def list_to_dict(lst):
    dict1 = {}
    for i, j in lst:
        dict1.update({i: j})
    return dict1


print('Dicitionary : ', list_to_dict(lst_tuple))


# o/p- Dicitionary :  {12: 45, 31: 23, 67: 55, 43: 84, 98: 32}
