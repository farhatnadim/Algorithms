import unittest
import numpy as np
from python.linear_algebra.modified_gram_schmidt import modified_gramshmidt


class TestModifiedGramSchmidt(unittest.TestCase):
    def check_qr(self, A):
        Q, R = modified_gramshmidt(A)
        n = A.shape[1]
        # Q has orthonormal columns
        np.testing.assert_allclose(Q.T @ Q, np.eye(n), atol=1e-10)
        # QR reconstructs A
        np.testing.assert_allclose(Q @ R, A, atol=1e-10)
        # R is upper triangular with positive diagonal
        np.testing.assert_allclose(R, np.triu(R), atol=1e-12)
        self.assertTrue((np.diag(R) > 0).all())

    def test_three_by_three(self):
        A = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 11.0]])
        self.check_qr(A)

    def test_rectangular_random(self):
        rng = np.random.default_rng(42)
        A = rng.random((5, 3))
        self.check_qr(A)

    def test_linearly_dependent_columns_raise(self):
        A = np.array([[1.0, 2.0], [2.0, 4.0]])  # second column = 2 * first
        with self.assertRaises(ValueError):
            modified_gramshmidt(A)


if __name__ == '__main__':
    unittest.main()
