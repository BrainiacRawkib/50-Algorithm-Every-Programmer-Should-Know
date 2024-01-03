"""
A matrix is a two-dimensional data structure with a fixed number of columns and rows. Each
element of a matrix can be referred to by its column and the row.
"""

import numpy as np


matrix_1 = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33]])


if __name__ == '__main__':
    print(matrix_1)
    print('Transposed Matrix!!!')
    print(matrix_1.transpose())
