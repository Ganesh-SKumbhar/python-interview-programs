# 16. Python Program for Insertion Sort

def insertion_sort(lst):
    for i in range(1, len(lst)):
        num = lst[i]

        j = i - 1
        while j >= 0 and num < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = num
        # print(lst)
    return lst


lst = [18, 12, 8, 25, 35, 6, 10, 21]

print('Sorted using insertion sort: ', insertion_sort(lst))

"""  o/p-
[12, 18, 8, 25, 35, 6, 10, 21]
[8, 12, 18, 25, 35, 6, 10, 21]
[8, 12, 18, 25, 35, 6, 10, 21]
[8, 12, 18, 25, 35, 6, 10, 21]
[6, 8, 12, 18, 25, 35, 10, 21]
[6, 8, 10, 12, 18, 25, 35, 21]
[6, 8, 10, 12, 18, 21, 25, 35]

Sorted using insertion sort:  [6, 8, 10, 12, 18, 21, 25, 35]

"""