import unittest
import numpy as np
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Search.Search import BinarySearchIterative, BinarySearch, BinarySearchRecursive, SecondLargest, closestPairBruteForce1D

class TestSearchAlgorithms(unittest.TestCase):
    def setUp(self):
        self.sorted_arrays = [
            np.array([1, 2, 3, 4, 5, 6]),
            np.array([1, 1, 1, 1]),
            np.array([1, 2, 3, 4]),
            np.array([1]),
            np.array([1, 2])
        ]
        
    def test_binary_search(self):
        for arr in self.sorted_arrays:
            for x in arr:
                self.assertTrue(BinarySearch(arr, x))
                self.assertTrue(BinarySearchIterative(arr, x))
                self.assertTrue(BinarySearchRecursive(arr, x))
            self.assertFalse(BinarySearchIterative(arr, max(arr) + 1))
            self.assertFalse(BinarySearchRecursive(arr, max(arr) + 1))
            self.assertFalse(BinarySearch(arr, max(arr) + 1))
            
    def test_second_largest(self):
        for arr in self.sorted_arrays:
            if len(arr) >= 2:
                expected = np.sort(np.unique(arr))[-2]
                result = SecondLargest(arr)
                self.assertEqual(result, expected)
                
    def test_closest_pair(self):
        arrays = [
            np.array([1, 4, 7, 2, 9, 3]),
            np.array([1.5, 2.5, 4.0, 8.0]),
            np.array([1, 2])
        ]
        for arr in arrays:
            p1, p2 = closestPairBruteForce1D(arr)
            min_diff = abs(p1 - p2)
            for i in range(len(arr)):
                for j in range(i+1, len(arr)):
                    self.assertGreaterEqual(abs(arr[i] - arr[j]), min_diff)

if __name__ == '__main__':
    unittest.main() 