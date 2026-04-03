import random
import argparse
import heapq
import statistics


def partition(array : list[int]) -> int:
    pivot_value = array[0]
    i = 1
    for j in range(1, len(array)): # range is exclusive
        if array[j] < pivot_value:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[0], array[i - 1] = array[i - 1], array[0]
    return i - 1


def DSelect(array, ith):
    if len(array) <= 5:
        return sorted(array)[ith]
    C = [statistics.median(array[i:i+5]) for i in range(0, len(array), 5)]
    p = DSelect(C, len(C) // 2)
    index_p = array.index(p)
    array[0], array[index_p] = array[index_p], array[0]
    j = partition(array)
    if j == ith:
        return array[j]
    elif j > ith:
        return DSelect(array[:j], ith)
    else:
        return DSelect(array[j + 1:], ith - j - 1)
if __name__ == '__main__':
    # pass the file name as an argument
    parser = argparse.ArgumentParser(description='DSelect')
    parser.add_argument('readFromFile', type=bool, help='Read from file or not')
    parser.add_argument('file', type=str, help='file name')
    parser.add_argument('ith', type=int, help='ith order statistic')

    args = parser.parse_args()

    # test the algorithm
    # read a text file that has an array with each element on a new line

    if (args.readFromFile):
        file_path = args.file
        with open(file_path) as f:
            array = f.readlines()
            array = [int(x.strip()) for x in array]

    #  finding the ith order statistic of the array using heapq
    ith = args.ith

    array1 = array.copy()
    assert( heapq.nsmallest(ith,array)[-1] == DSelect(array1, ith - 1))
    print(DSelect(array, ith - 1))