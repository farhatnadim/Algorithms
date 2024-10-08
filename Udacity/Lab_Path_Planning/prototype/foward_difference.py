import numpy as np
import matplotlib.pyplot as plt

robot_path = np.array([[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [4, 1], [4, 2], [3, 2], [3, 3], [3, 4], [3,5]])

print(robot_path)

# forward difference matrix 
def forward_difference_matrix(n):
    D = -1*np.eye(n, n)
    for i in range(n-1):
        D[i, i+1] = 1
        
    return D

# forward difference matrix
D = forward_difference_matrix(len(robot_path))
path_diff = np.dot(D, robot_path)

print(path_diff)