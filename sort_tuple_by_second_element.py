# 15. Sort a list of tuples by the second Item

def sort_by_second_item(lst):
    return sorted(lst,key=lambda x:x[1])

lst1 = [(12,45),(31,23),(67,55),(43,84),(98,32)]
print('Sorted list by second item: ',sort_by_second_item(lst1))

# o/p- Sorted list by second item:  [(31, 23), (98, 32), (12, 45), (67, 55), (43, 84)]
