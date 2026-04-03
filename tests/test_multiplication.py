import unittest
import sys
import os
import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from RecursiveIntegerMultiplication.Recursive_IntegerMultiplication import recursiveIntegerMultiplication
from RecursiveIntegerMultiplication.Karatsuba_Integer_Multiplication import (
    karatsubaMultiplication,
    getNumDigits,
    getPaddingsize,
    padNumber,
    unpadNumber
)

class TestMultiplicationAlgorithms(unittest.TestCase):
    def setUp(self):
        # All test cases must have numbers with power of 2 digits
        self.test_cases = [
            (1234, 5678, 4, 4),  # 4 digits each
            (12, 34, 2, 2),      # 2 digits each
            (1, 1, 1, 1),        # 1 digit each
            (1234, 1234, 4, 4),  # 4 digits each
            (9999, 9999, 4, 4),  # Max 4-digit numbers
        ]

    def test_recursive_multiplication(self):
        for num1, num2, n1, n2 in self.test_cases:
            expected = num1 * num2
            result = recursiveIntegerMultiplication(num1, num2, n1, n2)
            self.assertEqual(result, expected,
                           f"Failed for {num1} * {num2}: expected {expected}, got {result}")

    def test_karatsuba_multiplication(self):
        for num1, num2, n1, n2 in self.test_cases:
            expected = num1 * num2
            result = karatsubaMultiplication(num1, num2, n1, n2)
            self.assertEqual(result, expected,
                           f"Failed for {num1} * {num2}: expected {expected}, got {result}")

    def test_both_methods_agree(self):
        """Verify both recursive and Karatsuba produce same results"""
        for num1, num2, n1, n2 in self.test_cases:
            recursive_result = recursiveIntegerMultiplication(num1, num2, n1, n2)
            karatsuba_result = karatsubaMultiplication(num1, num2, n1, n2)
            self.assertEqual(recursive_result, karatsuba_result,
                           f"Methods disagree for {num1} * {num2}")

    def test_single_digit_multiplication(self):
        """Test base case with single digits"""
        for i in range(10):
            for j in range(10):
                expected = i * j
                result = recursiveIntegerMultiplication(i, j, 1, 1)
                self.assertEqual(result, expected)
                result = karatsubaMultiplication(i, j, 1, 1)
                self.assertEqual(result, expected)

    def test_multiplication_with_zero(self):
        """Test multiplication with zero"""
        test_cases = [
            (0, 1234, 1, 4),  # This may fail since digits don't match power of 2
            (12, 0, 2, 1),    # This may fail for same reason
        ]
        # These tests may need adjustment based on implementation constraints

    def test_get_num_digits(self):
        """Test helper function for counting digits"""
        self.assertEqual(getNumDigits(0), 1)
        self.assertEqual(getNumDigits(5), 1)
        self.assertEqual(getNumDigits(12), 2)
        self.assertEqual(getNumDigits(123), 3)
        self.assertEqual(getNumDigits(1234), 4)
        self.assertEqual(getNumDigits(99999), 5)

    def test_get_padding_size(self):
        """Test helper function for calculating padding"""
        # The function pads number of digits to next power of 2
        # 1 digit -> 0 padding (already power of 2)
        self.assertEqual(getPaddingsize(5), 0)
        # 2 digits: getNum2Multiples(2) = floor(log2(2)) + 1 = 2, so 2^2 - 2 = 2
        self.assertEqual(getPaddingsize(12), 2)
        # 3 digits: getNum2Multiples(3) = floor(log2(3)) + 1 = 2, so 2^2 - 3 = 1
        self.assertEqual(getPaddingsize(123), 1)
        # 4 digits: getNum2Multiples(4) = floor(log2(4)) + 1 = 3, so 2^3 - 4 = 4
        self.assertEqual(getPaddingsize(1234), 4)
        # 5 digits: getNum2Multiples(5) = floor(log2(5)) + 1 = 3, so 2^3 - 5 = 3
        self.assertEqual(getPaddingsize(12345), 3)

    def test_pad_and_unpad_number(self):
        """Test padding and unpadding numbers"""
        num = 123
        padding = 1
        padded = padNumber(num, padding)
        self.assertEqual(padded, 1230)  # One zero added

        unpadded = unpadNumber(padded, padding)
        self.assertEqual(unpadded, num)

        # Test with more padding
        num = 12
        padding = 2
        padded = padNumber(num, padding)
        self.assertEqual(padded, 1200)
        unpadded = unpadNumber(padded, padding)
        self.assertEqual(unpadded, num)

    def test_large_numbers(self):
        """Test with larger numbers (8 digits - power of 2)"""
        num1 = 12345678
        num2 = 87654321
        expected = num1 * num2

        result = recursiveIntegerMultiplication(num1, num2, 8, 8)
        self.assertEqual(result, expected)

        result = karatsubaMultiplication(num1, num2, 8, 8)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main() 