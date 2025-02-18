import unittest
import sys
import os
import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from RecursiveIntegerMultiplication.Recursive_IntegerMultiplication import recursiveIntegerMultiplication
from RecursiveIntegerMultiplication.Karatsuba_Integer_Multiplication import karatsubaMultiplication

class TestMultiplicationAlgorithms(unittest.TestCase):
    def setUp(self):
        # All test cases must have numbers with power of 2 digits
        self.test_cases = [
            (1234, 5678, 4, 4),  # 4 digits each
            (12, 34, 2, 2),      # 2 digits each
            (1, 1, 1, 1),        # 1 digit each
            (1234, 1234, 4, 4)   # 4 digits each
        ]
        
    def test_recursive_multiplication(self):
        for num1, num2, n1, n2 in self.test_cases:
            expected = num1 * num2
            result = recursiveIntegerMultiplication(num1, num2, n1, n2)
            self.assertEqual(result, expected)
            
    def test_karatsuba_multiplication(self):
        for num1, num2, n1, n2 in self.test_cases:
            expected = num1 * num2
            result = karatsubaMultiplication(num1, num2, n1, n2)
            self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main() 