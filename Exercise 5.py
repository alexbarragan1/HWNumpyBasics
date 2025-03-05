import numpy as np

array_1d = np.arange(1, 21)
print("1D Array:", array_1d)

matrix = array_1d.reshape(4, 5)
print("4x5 Matrix:\n", matrix)