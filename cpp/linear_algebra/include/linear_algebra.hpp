#ifndef ALGORITHMS_LINEAR_ALGEBRA_HPP
#define ALGORITHMS_LINEAR_ALGEBRA_HPP

#include <vector>
#include <utility>

namespace algorithms {

template<typename T>
using Matrix = std::vector<std::vector<T>>;

// TODO: User implements
// Dot product of two vectors of equal length.
// Reference: LinearAlgebra/Python/MatMul.py (VecDot)
template<typename T>
T vecDot(const std::vector<T>& a, const std::vector<T>& b);

// TODO: User implements
// Naive O(n^3) matrix multiplication; A is (m, k), B is (k, n).
// Reference: LinearAlgebra/Python/MatMul.py (MatMul)
template<typename T>
Matrix<T> matMul(const Matrix<T>& a, const Matrix<T>& b);

// TODO: User implements
// Recursive block matrix multiplication (8 sub-multiplications).
// Precondition: square matrices with power-of-2 dimension. Note the Python
// reference's 1x1 base case returns a scalar via NumPy broadcasting; here
// return a 1x1 matrix explicitly.
// Reference: LinearAlgebra/Python/MatMul.py (RecMatMult)
template<typename T>
Matrix<T> recMatMul(const Matrix<T>& x, const Matrix<T>& y);

// TODO: User implements
// Strassen's matrix multiplication (7 sub-multiplications).
// Precondition: square matrices with power-of-2 dimension.
// Reference: LinearAlgebra/Python/MatMul.py (strassenRecMat)
template<typename T>
Matrix<T> strassen(const Matrix<T>& x, const Matrix<T>& y);

// TODO: User implements
// Modified Gram-Schmidt QR decomposition: returns (Q, R).
// Throws on linearly dependent columns.
// Reference: LinearAlgebra/Python/ModfiedGramShmidt.py
// (note the Python filename typo; use the correct spelling here)
std::pair<Matrix<double>, Matrix<double>> modifiedGramSchmidt(const Matrix<double>& a);

} // namespace algorithms

#endif // ALGORITHMS_LINEAR_ALGEBRA_HPP
