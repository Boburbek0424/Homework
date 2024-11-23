# formula:
# normalized_value= value−min / max−min 

import numpy as np
random_matrix = np.random.rand(5, 5)
normalized_matrix = (random_matrix - random_matrix.min()) / (random_matrix.max() - random_matrix.min())
print(normalized_matrix)
