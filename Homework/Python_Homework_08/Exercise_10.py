import numpy as np
array = np.array([[5, 9, 3], [10, 2, 15], [6, 7, 8]])
array[np.arange(array.shape[0]), array.argmax(axis=1)] = 0
print(array)

