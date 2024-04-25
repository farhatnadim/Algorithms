'''this file implements the matrix multiplication algorithm'''
'''first we implement the dot product of two vectors'''
import numpy as np

def VecDot(a,b):
    dot = 0
    if a.shape[0] != b.shape[0]:
        return None
    for i in np.arange(a.shape[0]):
        dot += a[i] * b[i]
    return dot

def MatMul(A,B):
    if A.shape[1] != B.shape[0]:
        print("Make sure that M of columns of A is equal to N columns of B\n")
        return None
    C = np.zeros((A.shape[0],B.shape[1]))
    for row in np.arange(A.shape[0]):
        for column in np.arange(B.shape[1]):
            C[row,column] = VecDot(A[row,:],B[:,column])
    return C


def RecMatMult(X,Y):
    if X.shape[0] == 1 :
        return X[0][0] * Y[0][0]
    
    Z = np.zeros((X.shape[0],Y.shape[1]))
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
# now test the VecDot function
a = np.array([1,2,3])
b = np.array([4,5,6])


def strassenRecMat(X,Y):
    if X.shape[0] == 1 :
        return X[0][0] * Y[0][0]
    Z = np.zeros((X.shape[0],Y.shape[1]))
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


