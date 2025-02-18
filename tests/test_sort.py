import unittest
import numpy as np
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Sort.Sort import MergeSort, QuickSort, BubbleSort, InsertionSort

class TestSortAlgorithms(unittest.TestCase):
    def setUp(self):
        self.test_arrays = [
            np.array([5, 2, 8, 1, 9, 3]),
            np.array([1, 1, 1, 1]),
            np.array([4, 3, 2, 1]),
            np.array([1]),
            np.array([2, 1])
        ]
        
    def test_merge_sort(self):
        for arr in self.test_arrays:
            expected = np.sort(arr.copy())
            result = MergeSort(arr.copy())
            np.testing.assert_array_equal(result, expected)
            
    def test_quick_sort(self):
        for arr in self.test_arrays:
            expected = np.sort(arr.copy())
            arr_copy = arr.copy()
            QuickSort(arr_copy, 0, len(arr_copy))
            np.testing.assert_array_equal(arr_copy, expected)
            
    def test_bubble_sort(self):
        for arr in self.test_arrays:
            expected = np.sort(arr.copy())
            result = BubbleSort(arr.copy())
            np.testing.assert_array_equal(result, expected)
            
    def test_insertion_sort(self):
        for arr in self.test_arrays:
            expected = np.sort(arr.copy())
            result = InsertionSort(arr.copy())
            np.testing.assert_array_equal(result, expected)

if __name__ == '__main__':
    unittest.main() 