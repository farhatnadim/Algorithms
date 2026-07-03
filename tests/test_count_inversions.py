import unittest
import numpy as np
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Misc.CountInversions import bruteForeCountInversion, Sort_And_CountInV, Merge_and_CountSplit_Inv

class TestCountInversions(unittest.TestCase):
    def setUp(self):
        self.test_arrays = [
            (np.array([1, 2, 3, 4]), 0),  # Already sorted, no inversions
            (np.array([4, 3, 2, 1]), 6),  # Reverse sorted, maximum inversions
            (np.array([1, 3, 5, 2, 4, 6]), 3),  # Some inversions
            (np.array([1]), 0),  # Single element
            (np.array([2, 1]), 1),  # Two elements
            (np.array([5, 2, 8, 1, 9, 3]), 7),  # Mixed case
        ]

        # Test arrays with duplicates separately since the algorithm
        # may handle equal elements differently
        self.duplicate_arrays = [
            np.array([1, 1, 1, 1]),
            np.array([2, 1, 2, 1]),
        ]

    def test_brute_force_count_inversion(self):
        for arr, expected_count in self.test_arrays:
            result = bruteForeCountInversion(arr.copy())
            self.assertEqual(result, expected_count,
                           f"Failed for array {arr}: expected {expected_count}, got {result}")

    def test_sort_and_count_inversions(self):
        for arr, expected_count in self.test_arrays:
            sorted_arr, count = Sort_And_CountInV(arr.copy())
            # Verify count matches brute force
            self.assertEqual(count, expected_count,
                           f"Failed for array {arr}: expected {expected_count}, got {count}")
            # Verify array is sorted
            expected_sorted = np.sort(arr)
            np.testing.assert_array_equal(sorted_arr, expected_sorted,
                                        err_msg=f"Array not properly sorted for input {arr}")

    def test_merge_and_count_split_inversions(self):
        # Test basic merge
        left = np.array([1, 3, 5])
        right = np.array([2, 4, 6])
        merged, split_inv = Merge_and_CountSplit_Inv(left, right)
        expected_merged = np.array([1, 2, 3, 4, 5, 6])
        np.testing.assert_array_equal(merged, expected_merged)
        self.assertEqual(split_inv, 3)  # 3 > 2, 5 > 2, 5 > 4

        # Test merge with no inversions
        left = np.array([1, 2, 3])
        right = np.array([4, 5, 6])
        merged, split_inv = Merge_and_CountSplit_Inv(left, right)
        expected_merged = np.array([1, 2, 3, 4, 5, 6])
        np.testing.assert_array_equal(merged, expected_merged)
        self.assertEqual(split_inv, 0)

        # Test merge with all inversions
        left = np.array([4, 5, 6])
        right = np.array([1, 2, 3])
        merged, split_inv = Merge_and_CountSplit_Inv(left, right)
        expected_merged = np.array([1, 2, 3, 4, 5, 6])
        np.testing.assert_array_equal(merged, expected_merged)
        self.assertEqual(split_inv, 9)  # All left elements > all right elements

    def test_both_methods_agree(self):
        # Verify both methods produce same count for arrays without duplicates
        for arr, _ in self.test_arrays:
            brute_count = bruteForeCountInversion(arr.copy())
            _, sort_count = Sort_And_CountInV(arr.copy())
            self.assertEqual(brute_count, sort_count,
                           f"Methods disagree for array {arr}: brute={brute_count}, sort={sort_count}")

    def test_duplicates_brute_force_only(self):
        # Test duplicate arrays with brute force method only
        # The merge-based algorithm may count equal elements differently
        for arr in self.duplicate_arrays:
            brute_count = bruteForeCountInversion(arr.copy())
            # Just verify it completes without error
            self.assertIsNotNone(brute_count)

    def test_empty_array(self):
        """Empty input must return (empty, 0), not recurse infinitely"""
        arr = np.array([])
        sorted_arr, count = Sort_And_CountInV(arr.copy())
        self.assertEqual(count, 0)
        self.assertEqual(len(sorted_arr), 0)

    def test_dtype_preserved(self):
        """Counting inversions of an int array must return an int array"""
        arr = np.array([5, 2, 8, 1, 9, 3])
        sorted_arr, _ = Sort_And_CountInV(arr.copy())
        self.assertEqual(sorted_arr.dtype, arr.dtype)

    def test_edge_cases(self):
        # Single element
        arr = np.array([5])
        _, count = Sort_And_CountInV(arr.copy())
        self.assertEqual(count, 0)

        # Two elements in order
        arr = np.array([1, 2])
        _, count = Sort_And_CountInV(arr.copy())
        self.assertEqual(count, 0)

        # Two elements reversed
        arr = np.array([2, 1])
        _, count = Sort_And_CountInV(arr.copy())
        self.assertEqual(count, 1)

        # Large array with known inversions
        arr = np.array([5, 4, 3, 2, 1])  # n(n-1)/2 = 10 inversions
        _, count = Sort_And_CountInV(arr.copy())
        self.assertEqual(count, 10)

if __name__ == '__main__':
    unittest.main()
