'''This file reimplements the modified gramshmidt process depcited in Strang 5th edition , the code was implemented in Matlab'''
import numpy as np

def modified_gramshmidt(A : np.array) -> list[np.array, np.array] :
    # precompute memory 
    Q = np.zeros(A.shape)
    n = A.shape[1]
    R = np.zeros((n,n))
    
    # Define a small tolerance for zero-check
    tolerance = 1e-10 
    
    for j in np.arange(0,n):
        v = A[:,j].copy()
        for i in np.arange(0,j):
            R[i,j] = np.dot(Q[:,i],v)
            v = v - R[i,j]*Q[:,i]
        
        R[j,j] = np.linalg.norm(v)
        
        # --- FIX: Check for zero norm before dividing ---
        if R[j,j] < tolerance:
            # This indicates linear dependence. 
            # You could raise an error or just leave the column as zeros.
            # Raising an error is often better to signal a bad input.
            raise ValueError(f"Matrix has linearly dependent columns at column index {j}")

        Q[:,j] = v / R[j,j]
        
    return [Q,R]


def main():
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8,11]])
    Q, R = modified_gramshmidt(A)
    print("Q:", Q)
    print("R:", R)
    # compare against numpy's QR decomposition
    Q_np, R_np = np.linalg.qr(A)
    print("Q (numpy):", Q_np)
    print("R (numpy):", R_np)
    
main()