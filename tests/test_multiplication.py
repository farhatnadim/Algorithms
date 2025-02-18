import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from RecursiveIntegerMultiplication.Recursive_IntegerMultiplication import recursiveIntegerMultiplication
from RecursiveIntegerMultiplication.Karatsuba_Integer_Multiplication import karatsubaMultiplication

class TestMultiplicationAlgorithms(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            (1234, 5678, 4, 4),
            (12, 34, 2, 2),
            (1, 1, 1, 1),
            (123, 456, 3, 3)
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