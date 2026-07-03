'''this file implements the matrix multiplication algorithm'''
'''first we implement the dot product of two vectors'''
import numpy as np
import numpy.typing as npt


def VecDot(a: npt.NDArray, b: npt.NDArray):
    '''Dot product of two 1-D vectors of equal length.

    Raises ValueError if the lengths differ.'''
    if a.shape[0] != b.shape[0]:
        raise ValueError(f"vector lengths differ: {a.shape[0]} != {b.shape[0]}")
    dot = 0
    for i in np.arange(a.shape[0]):
        dot += a[i] * b[i]
    return dot


def MatMul(A: npt.NDArray, B: npt.NDArray) -> npt.NDArray:
    '''Naive O(n^3) matrix multiplication C = A @ B.

    A is (m, k), B is (k, n); raises ValueError if the inner dimensions differ.
    The result dtype follows NumPy promotion of the operand dtypes
    (int x int stays int).'''
    if A.shape[1] != B.shape[0]:
        raise ValueError(
            f"inner dimensions differ: A is {A.shape}, B is {B.shape}")
    C = np.zeros((A.shape[0],B.shape[1]), dtype=np.result_type(A.dtype, B.dtype))
    for row in np.arange(A.shape[0]):
        for column in np.arange(B.shape[1]):
            C[row,column] = VecDot(A[row,:],B[:,column])
    return C


def RecMatMult(X: npt.NDArray, Y: npt.NDArray):
    '''Recursive block matrix multiplication (8 sub-multiplications).

    Precondition: X and Y are square matrices whose dimension is a power of 2
    (no padding is performed). The 1x1 base case returns a SCALAR, which NumPy
    broadcasting assigns into the 2D quadrant slices below — a port to C++/Lean
    must return a 1x1 matrix (or handle the scalar case) explicitly.'''
    if X.shape[0] == 1 :
        return X[0][0] * Y[0][0]

    Z = np.zeros((X.shape[0],Y.shape[1]), dtype=np.result_type(X.dtype, Y.dtype))
    # upper left 
    A = X[:X.shape[0]//2,:X.shape[1]//2]
    # upper Right
    B = X[:X.shape[0]//2,X.shape[1]//2:]
    # lower left 
    C = X[X.shape[0]//2:,:X.shape[1]//2]
    # lower right 
    D = X[X.shape[0]//2:,X.shape[1]//2:]

    E = Y[:Y.shape[0]//2,:Y.shape[1]//2]
    # upper light
    F = Y[:Y.shape[0]//2,Y.shape[1]//2:]
    # lower left 
    G = Y[Y.shape[0]//2:,:Y.shape[1]//2]
    # lower right 
    H = Y[Y.shape[0]//2:,Y.shape[1]//2:]

    AE = RecMatMult(A,E)
    BG = RecMatMult(B,G)
    AF = RecMatMult(A,F)
    BH = RecMatMult(B,H)
    CE = RecMatMult(C,E)
    DG = RecMatMult(D,G)
    CF = RecMatMult(C,F)
    DH = RecMatMult(D,H)
    Z[:X.shape[0]//2,:Y.shape[1]//2] =  AE + BG
    Z[:X.shape[0]//2,Y.shape[1]//2:] =  AF + BH
    Z[X.shape[0]//2:,:Y.shape[1]//2] =  CE + DG
    Z[X.shape[0]//2:,Y.shape[1]//2:] = CF + DH
    return Z


def strassenRecMat(X: npt.NDArray, Y: npt.NDArray):
    '''Strassen's matrix multiplication (7 sub-multiplications).

    Precondition: X and Y are square matrices whose dimension is a power of 2
    (no padding is performed). As in RecMatMult, the 1x1 base case returns a
    scalar that is assigned into the quadrant slices via broadcasting.'''
    if X.shape[0] == 1 :
        return X[0][0] * Y[0][0]
    Z = np.zeros((X.shape[0],Y.shape[1]), dtype=np.result_type(X.dtype, Y.dtype))
    # upper left 
    A = X[:X.shape[0]//2,:X.shape[1]//2]
    # upper Right
    B = X[:X.shape[0]//2,X.shape[1]//2:]
    # lower left 
    C = X[X.shape[0]//2:,:X.shape[1]//2]
    # lower right 
    D = X[X.shape[0]//2:,X.shape[1]//2:]

    E = Y[:Y.shape[0]//2,:Y.shape[1]//2]
    # upper light
    F = Y[:Y.shape[0]//2,Y.shape[1]//2:]
    # lower left 
    G = Y[Y.shape[0]//2:,:Y.shape[1]//2]
    # lower right 
    H = Y[Y.shape[0]//2:,Y.shape[1]//2:]

    P1 = strassenRecMat(A,F-H)
    P2 = strassenRecMat(A+B,H)
    P3 = strassenRecMat(C+D,E)
    P4 = strassenRecMat(D,G-E)
    P5 = strassenRecMat(A+D,E+H)
    P6 = strassenRecMat(B-D,G+H)
    P7 = strassenRecMat(A-C,E+F)

    Z[:X.shape[0]//2,:Y.shape[1]//2] =  P5 + P4 - P2 + P6
    Z[:X.shape[0]//2,Y.shape[1]//2:] =  P1 + P2
    Z[X.shape[0]//2:,:Y.shape[1]//2] =  P3 + P4
    Z[X.shape[0]//2:,Y.shape[1]//2:] =  P1 + P5 - P3 - P7

    return Z


