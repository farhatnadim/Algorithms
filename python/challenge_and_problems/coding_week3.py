''' Implements Programming Assignment 3 of course "Algorithms: Design and Analysis, Part 1" on Coursera.'''

import numpy as np  #import numpy library
def partition(array, left, right):
    """
    Partition the array into two parts - one with elements smaller than a pivot value and another with elements greater than the pivot value.

    Args:
    - array: The input array to be partitioned.
    - left: The starting index of the partition.
    - right: The ending index of the partition.

    Returns:
    - pivot_index: The index of the pivot element after partitioning the array.
    """

    if left >= right:
        return -1

    pivot_value = array[left]
    lesser_index = left + 1

    for greater_index in range(left + 1, right):
        if array[greater_index] < pivot_value:
            array[lesser_index], array[greater_index] = array[greater_index], array[lesser_index]
            lesser_index += 1

    pivot_index = lesser_index - 1
    array[left], array[pivot_index] = array[pivot_index], array[left]

    return pivot_index

def QuickSort(array, left, right,count_recursion, type = 'last'):
    if left >= right:
        return
    # m-1 is used to count the number of recursions
    count_recursion[0] += right - left - 1
    if type == 'random':
        pivot_index = np.random.randint(left, right)
    elif type == 'median':
        mid = left + (right - left - 1) // 2
        first, last = left, right - 1
        # Directly find the median of the first, middle, and last elements
        trio = [(array[first], first), (array[mid], mid), (array[last], last)]
        trio.sort(key=lambda x: x[0])
        pivot_index = trio[1][1] # Get the index of the median value
    elif type == 'first':
        pivot_index = left
    elif type == 'last':
        pivot_index = right - 1
    else:
        print('Invalid type')
    array[left], array[pivot_index] = array[pivot_index], array[left]
    new_pivot_index = partition(array, left, right)
    QuickSort(array, left, new_pivot_index,count_recursion)
    QuickSort(array, new_pivot_index + 1, right,count_recursion)
    
# Test the QuickSort function
# generate a random array of integers


# read text file from disk
with open(r'C:\Users\nadim\Downloads\QuickSort.txt') as f:
    array = f.readlines()
    array = [int(x.strip()) for x in array]
    
#print('Original array:', array)
count_recursion = []
count_recursion.append(0)
QuickSort(array, 0, len(array), count_recursion)
print('Count Recursion:', count_recursion)
# print the sorted array
#print('Sorted array:', array)