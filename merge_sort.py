# 19. Python Program for Merge Sort
# MergeSort in Python


def merge_sort(array):
    if len(array) > 1:

        #  mid is the point where the array is divided into two subarrays
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        # Sort the two halves
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Until we reach either end of either left or right, pick larger among
        # elements left and right and place them in the correct position at A[p..r]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        # When we run out of elements in either left or right,
        # pick up the remaining elements and put in A[p..r]
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


# Print the array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


lst = [18, 12, 8, 25, 35, 6, 10, 21]
merge_sort(lst)
printList(lst)


""" o/p- 
6 8 10 12 18 21 25 35 
"""