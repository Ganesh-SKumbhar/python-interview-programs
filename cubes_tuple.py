# 14. Create a list of tuples from the given list having a number and its cube in each tuple
lst = [1, 3, 5, 7, 9, 11]


def ret_list_tuple_cubes(lst):
    return [(i, i ** 3) for i in lst]


print('list of tuples : ', ret_list_tuple_cubes(lst))



# o/p- list of tuples :  [(1, 1), (3, 27), (5, 125), (7, 343), (9, 729), (11, 1331)]