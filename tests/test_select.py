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

if __name__ == '__main__':
    unittest.main() 