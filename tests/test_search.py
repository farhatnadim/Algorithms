import unittest
import numpy as np
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Search.Search import (BinarySearchIterative, BinarySearch, BinarySearchRecursive, 
                         SecondLargest, closestPairBruteForce1D, ThreeSumBruteForce, 
                         ThreeSumQuick, Rselect)

class TestSearchAlgorithms(unittest.TestCase):
    def setUp(self):
        self.sorted_arrays = [
            np.array([1, 2, 3, 4, 5, 6]),
            np.array([1, 1, 1, 1]),
            np.array([1, 2, 3, 4]),
            np.array([1]),
            np.array([1, 2])
        ]
        
        self.unsorted_arrays = [
            np.array([5, 2, 8, 1, 9, 3]),
            np.array([4, 3, 2, 1]),
            np.array([2, 1])
        ]
        
    def test_binary_search(self):
        for arr in self.sorted_arrays:
            for x in arr:
                self.assertNotEqual(BinarySearchIterative(arr, x), -1)
                self.assertNotEqual(BinarySearchRecursive(arr, x, 0, len(arr)-1), -1)
                self.assertNotEqual(BinarySearch(arr, x), -1)
            # Test for element not in array
            self.assertEqual(BinarySearchIterative(arr, max(arr) + 1), -1)
            self.assertEqual(BinarySearchRecursive(arr, max(arr) + 1, 0, len(arr)-1), -1)
            self.assertEqual(BinarySearch(arr, max(arr) + 1), -1)
            
    def test_second_largest(self):
        for arr in self.unsorted_arrays:
            if len(arr) >= 2:
                expected = np.sort(np.unique(arr))[-2]
                result = SecondLargest(arr)[1]  # SecondLargest returns [largest, second_largest]
                self.assertEqual(result, expected)
                
    def test_three_sum(self):
        test_arrays = [
            np.array([-1, 0, 1]),  # Should find one triplet
            np.array([0, 0, 0]),   # Should find one triplet
            np.array([1, 2, 3]),   # Should find no triplets
        ]
        
        for arr in test_arrays:
            count_bf, triplets_bf = ThreeSumBruteForce(arr)
            count_quick, triplets_quick = ThreeSumQuick(arr.copy())  # Need to use copy as sorting modifies array
            self.assertEqual(count_bf, count_quick)
            
    def test_rselect(self):
        for arr in self.unsorted_arrays:
            sorted_arr = np.sort(arr)
            for i in range(len(arr)):
                arr_copy = arr.copy()
                position = Rselect(arr_copy.tolist(), 0, len(arr_copy), i)  # Convert to list as required by Rselect
                self.assertEqual(sorted_arr[i], arr_copy[position])

    def test_closest_pair_1d(self):
        # Test empty array
        with self.assertRaises(ValueError):
            closestPairBruteForce1D(np.array([]))
            
        # Test single element array
        with self.assertRaises(ValueError):
            closestPairBruteForce1D(np.array([1]))
            
        # Test valid case with known closest pair
        arr = np.array([1, 4, 2, 9, 3])  # 2 and 3 should be closest
        p1, p2 = closestPairBruteForce1D(arr)
        min_diff = abs(p1 - p2)
        # Verify this is indeed the minimum difference
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                self.assertGreaterEqual(abs(arr[i] - arr[j]), min_diff)

if __name__ == '__main__':
    unittest.main() 