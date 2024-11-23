import numpy as np
arr = np.array([1, 2, 0, 0, 4, 0])
non_zero_indexes = np.nonzero(arr)[0]
print(non_zero_indexes.tolist())