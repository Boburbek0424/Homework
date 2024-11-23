import numpy as np
matrix = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
try:
    inverse_matrix = np.linalg.inv(matrix)
    print(inverse_matrix)
except np.linalg.LinAlgError:
    print("Matrix is singular and cannot be inverted.")
