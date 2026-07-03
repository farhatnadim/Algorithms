import unittest
import numpy as np
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from LinearAlgebra.Python.MatMul import VecDot, MatMul, RecMatMult, strassenRecMat


class TestVecDot(unittest.TestCase):
    def test_matches_numpy(self):
        rng = np.random.default_rng(0)
        a = rng.integers(-10, 10, 6)
        b = rng.integers(-10, 10, 6)
        self.assertEqual(VecDot(a, b), np.dot(a, b))

    def test_length_mismatch_raises(self):
        with self.assertRaises(ValueError):
            VecDot(np.array([1, 2]), np.array([1, 2, 3]))


class TestMatMul(unittest.TestCase):
    def test_matches_numpy_int(self):
        rng = np.random.default_rng(1)
        A = rng.integers(-5, 5, (3, 4))
        B = rng.integers(-5, 5, (4, 2))
        C = MatMul(A, B)
        np.testing.assert_array_equal(C, A @ B)
        self.assertEqual(C.dtype, np.result_type(A.dtype, B.dtype))

    def test_matches_numpy_float(self):
        rng = np.random.default_rng(2)
        A = rng.random((4, 3))
        B = rng.random((3, 5))
        np.testing.assert_allclose(MatMul(A, B), A @ B)

    def test_shape_mismatch_raises(self):
        with self.assertRaises(ValueError):
            MatMul(np.zeros((2, 3)), np.zeros((2, 3)))


class TestRecursiveMatMul(unittest.TestCase):
    """RecMatMult and strassenRecMat require square power-of-2 matrices."""

    def test_rec_mat_mult_matches_numpy(self):
        rng = np.random.default_rng(3)
        for n in (2, 4, 8):
            X = rng.integers(-5, 5, (n, n))
            Y = rng.integers(-5, 5, (n, n))
            np.testing.assert_array_equal(RecMatMult(X, Y), X @ Y)

    def test_strassen_matches_numpy_int(self):
        rng = np.random.default_rng(4)
        for n in (2, 4, 8):
            X = rng.integers(-5, 5, (n, n))
            Y = rng.integers(-5, 5, (n, n))
            np.testing.assert_array_equal(strassenRecMat(X, Y), X @ Y)

    def test_strassen_matches_numpy_float(self):
        rng = np.random.default_rng(5)
        X = rng.random((8, 8))
        Y = rng.random((8, 8))
        np.testing.assert_allclose(strassenRecMat(X, Y), X @ Y)

    def test_one_by_one_base_case(self):
        X = np.array([[3]])
        Y = np.array([[7]])
        # the 1x1 base case returns a scalar by design (see MatMul.py docstring)
        self.assertEqual(RecMatMult(X, Y), 21)
        self.assertEqual(strassenRecMat(X, Y), 21)


if __name__ == '__main__':
    unittest.main()
