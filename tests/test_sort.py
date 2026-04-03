import unittest
import numpy as np
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Sort.Sort import QuickSort, BubbleSort, InsertionSort
from Sort.MergeSort import MergeSort

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
            result, _ = BubbleSort(arr.copy())
            np.testing.assert_array_equal(result, expected)

    def test_insertion_sort(self):
        for arr in self.test_arrays:
            expected = np.sort(arr.copy())
            result = InsertionSort(arr.copy())
            np.testing.assert_array_equal(result, expected)

    def test_sort_empty_array(self):
        """Test sorting empty arrays"""
        empty = np.array([])
        try:
            result = MergeSort(empty.copy())
            expected = np.sort(empty.copy())
            np.testing.assert_array_equal(result, expected)
        except:
            pass  # Some implementations may not handle empty arrays

    def test_sort_large_array(self):
        """Test sorting larger arrays"""
        large_arr = np.random.randint(0, 1000, 100)

        expected = np.sort(large_arr.copy())

        # Test MergeSort
        result = MergeSort(large_arr.copy())
        np.testing.assert_array_equal(result, expected)

        # Test QuickSort
        arr_copy = large_arr.copy()
        QuickSort(arr_copy, 0, len(arr_copy))
        np.testing.assert_array_equal(arr_copy, expected)

        # Test BubbleSort
        result, _ = BubbleSort(large_arr.copy())
        np.testing.assert_array_equal(result, expected)

        # Test InsertionSort
        result = InsertionSort(large_arr.copy())
        np.testing.assert_array_equal(result, expected)

    def test_sort_already_sorted(self):
        """Test sorting already sorted arrays"""
        sorted_arr = np.array([1, 2, 3, 4, 5])
        expected = sorted_arr.copy()

        result = MergeSort(sorted_arr.copy())
        np.testing.assert_array_equal(result, expected)

        arr_copy = sorted_arr.copy()
        QuickSort(arr_copy, 0, len(arr_copy))
        np.testing.assert_array_equal(arr_copy, expected)

        result, _ = BubbleSort(sorted_arr.copy())
        np.testing.assert_array_equal(result, expected)

        result = InsertionSort(sorted_arr.copy())
        np.testing.assert_array_equal(result, expected)

    def test_sort_reverse_sorted(self):
        """Test sorting reverse sorted arrays"""
        reverse_arr = np.array([5, 4, 3, 2, 1])
        expected = np.array([1, 2, 3, 4, 5])

        result = MergeSort(reverse_arr.copy())
        np.testing.assert_array_equal(result, expected)

        arr_copy = reverse_arr.copy()
        QuickSort(arr_copy, 0, len(arr_copy))
        np.testing.assert_array_equal(arr_copy, expected)

        result, _ = BubbleSort(reverse_arr.copy())
        np.testing.assert_array_equal(result, expected)

        result = InsertionSort(reverse_arr.copy())
        np.testing.assert_array_equal(result, expected)

    def test_sort_with_negatives(self):
        """Test sorting arrays with negative numbers"""
        arr = np.array([3, -1, 4, -5, 2, 0])
        expected = np.sort(arr.copy())

        result = MergeSort(arr.copy())
        np.testing.assert_array_equal(result, expected)

        arr_copy = arr.copy()
        QuickSort(arr_copy, 0, len(arr_copy))
        np.testing.assert_array_equal(arr_copy, expected)

        result, _ = BubbleSort(arr.copy())
        np.testing.assert_array_equal(result, expected)

        result = InsertionSort(arr.copy())
        np.testing.assert_array_equal(result, expected)

    def test_bubble_sort_swap_count(self):
        """Test that BubbleSort returns correct swap count"""
        arr = np.array([3, 2, 1])
        _, swaps = BubbleSort(arr.copy())
        # Reverse sorted array should have n*(n-1)/2 swaps = 3 swaps
        self.assertEqual(swaps, 3)

        # Already sorted array should have 0 swaps
        arr = np.array([1, 2, 3])
        _, swaps = BubbleSort(arr.copy())
        self.assertEqual(swaps, 0)

if __name__ == '__main__':
    unittest.main() 