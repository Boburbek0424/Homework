import numpy as np
my_array = np.array([1, 3, 5, 11, 15, 20, 25])
target = 14
closest_value = my_array[np.abs(my_array - target).argmin()]
print(closest_value)
