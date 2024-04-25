'''this program implement count inversions algorithm using brute force and divide and conquer method'''
import numpy as np
# Brute force method

def bruteForeCountInversion(array):
    '''this function counts the number of inversions in an array using brute force method'''
    '''input : array of integers'''
    '''output : number of inversions in the array'''
    '''time complexity : O(n^2)'''
    inversionCount = 0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] > array[j]:
                inversionCount += 1
    return inversionCount

def Merge_and_CountSplit_Inv(left,right):
    '''this function merges two sorted arrays and counts the number of split inversions'''
    '''input : left and right arrays'''
    '''output : merged array and number of split inversions'''
    '''time complexity : O(n)'''
    i = 0
    j = 0
    k = 0
    splitInv = 0    
    merged = np.zeros(left.shape[0]+right.shape[0])
    # while we are within the limits of the arrays
    # we merge the arrays
    while (i < left.shape[0]) and (j < right.shape[0]):
        if left[i] < right[j]:
            merged[k] = left[i]
            i += 1
            
        else: 
            merged[k] = right[j] 
            j += 1
            splitInv += left.shape[0] - i
            
        k+=1
    # we exited the above loop due to one of the arrays being exhausted
    # we now copy the remaining elements from the other array
    # if we are still within the limits of the right array we copy the remaining elements
    while i < left.shape[0]:
        merged[k] = left[i]
        i += 1
        k += 1
    # if we are still within the limits of the left array we copy the remaining elements
    while j < right.shape[0]:
        merged[k] = right[j]
        j += 1
        k += 1
        # we return the merged array
    return merged, splitInv

def Sort_And_CountInV(array):
    '''This function implements the merge sort algorithm
    Input: numpy array of numbers
    Output: sorted numpy array of numbers
    as presented in the book, Algorithms Illuminated by Tim Roughgarden'''
    leftInv = 0
    rightInv = 0
    splitInv = 0
    merged = np.zeros(array.shape[0])
    # base case
    if array.shape[0] == 1:
        return array,0
    else:
        # general case
        # we split the array in two and recursively call mergeSort
        left,leftInv = Sort_And_CountInV(array[0:array.shape[0]//2]) 
        right,rightInv = Sort_And_CountInV(array[array.shape[0]//2:])
        
        merged, splitInv = Merge_and_CountSplit_Inv(left,right)
        return merged, leftInv + rightInv + splitInv