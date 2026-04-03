import numpy as np
from typing import TypeVar, Any
from numpy.typing import NDArray

# Type variable for numeric types - similar to Rust's generic T with trait bounds
# In Rust: T: Clone + PartialOrd + Debug
# In Python: TypeVar bound to np.floating (which covers most numeric operations)
NumericType = TypeVar('NumericType', bound=np.floating[Any])

# Merge function - combines two sorted arrays into a single sorted array
# This mirrors the Rust function signature: fn merge<T>(left: &[T], right: &[T]) -> Vec<T>
def Merge(left: NDArray[NumericType], right: NDArray[NumericType], merged: NDArray[NumericType]) -> NDArray[NumericType]:
    i: int = 0  # left array index - equivalent to Rust's let mut i = 0
    j: int = 0  # right array index - equivalent to Rust's let mut j = 0 
    k: int = 0  # merged array index
    # while we are within the limits of the arrays
    # we merge the arrays
    while (i < left.shape[0]) and (j < right.shape[0]):
        if left[i] < right[j]:
            merged[k] = left[i]
            i += 1        
        else: 
            merged[k] = right[j] 
            j += 1
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
    return merged 



def MergeSort(array: NDArray[NumericType]) -> NDArray[NumericType]:
    '''MergeSort function - recursive merge sort implementation
    This mirrors the Rust function: pub fn merge_sort<T>(array: &[T]) -> Vec<T>
    
    Input: numpy array of numbers (equivalent to Rust's &[T])
    Output: sorted numpy array of numbers (equivalent to Rust's Vec<T>)
    as presented in the book, Algorithms Illuminated by Tim Roughgarden'''
    
    merged: NDArray[NumericType] = np.zeros(array.shape[0], dtype=array.dtype)
    # base case - handle both empty and single element arrays
    if array.shape[0] <= 1:
        return array
    else:
        # General case - split array and recursively sort
        # This mirrors the Rust implementation's array slicing
        mid: int = array.shape[0] // 2  # equivalent to Rust's let mid = array.len() / 2
        
        # In Rust, we split the slice into two parts: &array[mid..] and &array[0..mid]
        left: NDArray[NumericType] = MergeSort(array[mid:])     # Right half (like Rust)
        right: NDArray[NumericType] = MergeSort(array[0:mid])   # Left half (like Rust)
        
        # Merge the sorted halves
        Merge(left, right, merged)
        return merged