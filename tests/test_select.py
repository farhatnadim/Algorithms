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
            np.array([5, 2, 8, 1, 9, 3]),
            np.array([1, 1, 1, 1]),
            np.array([4, 3, 2, 1]),
            np.array([1]),
            np.array([2, 1])
        ]
        
    def test_random_select(self):
        for arr in self.test_arrays:
            for i in range(len(arr)):
                expected = np.sort(arr)[i]
                result = RSelect(arr.copy(), i)
                self.assertEqual(result, expected)
                
    def test_deterministic_select(self):
        for arr in self.test_arrays:
            for i in range(len(arr)):
                expected = np.sort(arr)[i]
                result = DSelect(arr.copy(), i)
                self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main() 