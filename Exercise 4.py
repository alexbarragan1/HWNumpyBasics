import numpy as np

matrix = np.arange(1, 26).reshape(5, 5)
print("Original Matrix:\n", matrix)

third_row = matrix[2, :]
print("Third Row:", third_row)

last_two_columns = matrix[:, -2:]
print("Last Two Columns:\n", last_two_columns)

submatrix = matrix[1:4, 1:4]
print("3x3 Submatrix:\n", submatrix)