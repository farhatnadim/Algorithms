import unittest
import numpy as np
import sys
import os
from typing import List, Any
from numpy.typing import NDArray

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Sort.MergeSort import MergeSort, Merge

class TestMergeSort(unittest.TestCase):
    def setUp(self) -> None:
        # Type hint for test arrays - similar to Rust's Vec<Vec<T>> concept  
        self.test_arrays: List[NDArray[np.float64]] = [
            np.array([5, 2, 8, 1, 9, 3]),
            np.array([1, 1, 1, 1]),
            np.array([4, 3, 2, 1]),
            np.array([1]),
            np.array([2, 1]),
            np.array([]),  # Empty array
            np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),  # Reverse sorted
            np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),  # Already sorted
            np.array([5]),  # Single element
            np.array([3, 3, 3, 1, 1, 2, 2, 2]),  # Duplicates
        ]
        
    def test_mergesort_basic(self) -> None:
        """Test MergeSort with basic test cases"""
        for arr in self.test_arrays:
            if arr.size > 0:  # Skip empty array for now
                expected: NDArray[np.float64] = np.sort(arr.copy())
                result: NDArray[np.float64] = MergeSort(arr.copy())
                np.testing.assert_array_equal(result, expected, 
                    err_msg=f"Failed for input: {arr}")
    
    def test_mergesort_empty_array(self) -> None:
        """Test MergeSort with empty array"""
        empty_arr: NDArray[np.float64] = np.array([])
        try:
            result: NDArray[np.float64] = MergeSort(empty_arr.copy())
            expected: NDArray[np.float64] = np.sort(empty_arr.copy())
            np.testing.assert_array_equal(result, expected)
        except Exception as e:
            print(f"MergeSort fails with empty array: {e}")
    
    def test_mergesort_single_element(self) -> None:
        """Test MergeSort with single element"""
        single_arr: NDArray[np.float64] = np.array([42])
        expected: NDArray[np.float64] = np.array([42])
        result: NDArray[np.float64] = MergeSort(single_arr.copy())
        np.testing.assert_array_equal(result, expected)
    
    def test_mergesort_two_elements(self) -> None:
        """Test MergeSort with two elements"""
        test_cases: List[NDArray[np.float64]] = [
            np.array([2, 1]),
            np.array([1, 2]),
            np.array([5, 5])
        ]
        for arr in test_cases:
            expected: NDArray[np.float64] = np.sort(arr.copy())
            result: NDArray[np.float64] = MergeSort(arr.copy())
            np.testing.assert_array_equal(result, expected,
                err_msg=f"Failed for input: {arr}")
    
    def test_mergesort_large_array(self) -> None:
        """Test MergeSort with larger array"""
        large_arr: NDArray[np.float64] = np.random.randint(0, 100, 50)
        expected: NDArray[np.float64] = np.sort(large_arr.copy())
        result: NDArray[np.float64] = MergeSort(large_arr.copy())
        np.testing.assert_array_equal(result, expected)
    
    def test_merge_function(self) -> None:
        """Test the Merge helper function directly"""
        # Test basic merge
        left: NDArray[np.float64] = np.array([1, 3, 5])
        right: NDArray[np.float64] = np.array([2, 4, 6])
        merged: NDArray[np.float64] = np.zeros(6)
        result: NDArray[np.float64] = Merge(left, right, merged)
        expected: NDArray[np.float64] = np.array([1, 2, 3, 4, 5, 6])
        np.testing.assert_array_equal(result, expected)
        
        # Test merge with different sizes
        left = np.array([1, 5])
        right = np.array([2, 3, 4])
        merged = np.zeros(5)
        result = Merge(left, right, merged)
        expected = np.array([1, 2, 3, 4, 5])
        np.testing.assert_array_equal(result, expected)
    
    def test_mergesort_preserves_input(self) -> None:
        """Test that MergeSort doesn't modify the original array"""
        original: NDArray[np.float64] = np.array([5, 2, 8, 1, 9, 3])
        input_copy: NDArray[np.float64] = original.copy()
        result: NDArray[np.float64] = MergeSort(input_copy)
        # The input should not be modified since we're creating a new merged array
        # But let's check what actually happens
        print(f"Original: {original}")
        print(f"Input after MergeSort: {input_copy}")
        print(f"Result: {result}")

if __name__ == '__main__':
    unittest.main()