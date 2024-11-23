import numpy as np
array = np.array([2, 3, 2, 5, 8, 3, 3, 7, 2, 3, 5, 5, 5, 5])
most_common = np.bincount(array).argmax()
print(most_common)
