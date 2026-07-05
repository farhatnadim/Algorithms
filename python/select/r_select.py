import random
import argparse
import heapq


def partition(array : list[int]) -> int:
    pivot_value = array[0]
    i = 1
    for j in range(1, len(array)): # range is exclusive
        if array[j] < pivot_value:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[0], array[i - 1] = array[i - 1], array[0]
    return i - 1

def RSelect(array : list[int], ith : int) -> int:
    '''Value-returning randomized select over a copy-sliced list (contrast with
    Search.Search.Rselect, which is the index-returning, in-place, windowed variant).'''
    if not array:
        raise ValueError("array must be non-empty")
    if not 0 <= ith < len(array):
        raise ValueError(f"ith must be in [0, {len(array) - 1}]")
    if len(array) == 1:
        return array[0]
    pivot_index = random.randint(0, len(array) - 1) # randint int is inclusive
    array[0], array[pivot_index] = array[pivot_index], array[0]
    j = partition(array)
    if j == ith:
        return array[j]
    elif j > ith:
        return RSelect(array[:j], ith) # skips the pivot element
    else:
        return RSelect(array[j + 1:], ith - j - 1) # skips the pivot element

if __name__ == '__main__':
    # pass the file name as an argument
    parser = argparse.ArgumentParser(description='RSelect')
    parser.add_argument('file', type=str, help='file name')
    parser.add_argument('ith', type=int, help='ith order statistic')

    args = parser.parse_args()

    # read a text file that has an array with each element on a new line
    with open(args.file) as f:
        array = [int(x.strip()) for x in f.readlines()]

    #  finding the ith order statistic of the array using heapq
    ith = args.ith

    array1 = array.copy()
    assert( heapq.nsmallest(ith,array)[-1] == RSelect(array1, ith-1))
    print(RSelect(array, ith - 1))