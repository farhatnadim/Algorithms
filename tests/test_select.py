import unittest
import numpy as np
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Select.Python.RSelect import RSelect
from Select.Python.DSelect import DSelect

class TestSelectAlgorithms(unittest.TestCase):
    def setUp(self):
        self.test_arrays = [
            [5, 2, 8, 1, 9, 3],  # Using lists instead of numpy arrays
            [4, 3, 2, 1],
            [2, 1],
            [1],
        ]
        
    def test_random_select(self):
        for arr in self.test_arrays:
            for i in range(len(arr)):
                arr_copy = arr.copy()
                sorted_copy = sorted(arr)
                result = RSelect(arr_copy, i)
                self.assertEqual(result, sorted_copy[i])
                
    def test_deterministic_select(self):
        for arr in self.test_arrays:
            for i in range(len(arr)):
                arr_copy = arr.copy()
                sorted_copy = sorted(arr)
                result = DSelect(arr_copy, i)
                self.assertEqual(result, sorted_copy[i])
                
    def test_edge_cases(self):
        # Test single element array
        arr = [1]
        self.assertEqual(RSelect(arr.copy(), 0), 1)
        self.assertEqual(DSelect(arr.copy(), 0), 1)

        # Test array with duplicate elements
        arr = [3, 3, 3, 3]
        for i in range(len(arr)):
            self.assertEqual(RSelect(arr.copy(), i), 3)
            self.assertEqual(DSelect(arr.copy(), i), 3)

    def test_larger_arrays_with_even_tail_group(self):
        """Arrays of 14 and 23 elements force even-sized tail groups in
        DSelect's median-of-medians (the old statistics.median crashed here)"""
        arrays = [
            [42, 7, 19, 3, 88, 51, 64, 12, 95, 27, 33, 76, 8, 59],           # 5+5+4
            list(range(23, 0, -1)),                                           # 5*4+3
        ]
        for arr in arrays:
            sorted_copy = sorted(arr)
            for i in range(len(arr)):
                self.assertEqual(DSelect(arr.copy(), i), sorted_copy[i])
                self.assertEqual(RSelect(arr.copy(), i), sorted_copy[i])

    def test_invalid_inputs_raise(self):
        """Empty arrays and out-of-range order statistics raise ValueError"""
        with self.assertRaises(ValueError):
            RSelect([], 0)
        with self.assertRaises(ValueError):
            DSelect([], 0)
        with self.assertRaises(ValueError):
            RSelect([1, 2, 3], 3)
        with self.assertRaises(ValueError):
            DSelect([1, 2, 3], -1)

if __name__ == '__main__':
    unittest.main() 