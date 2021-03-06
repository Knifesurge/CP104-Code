"""
------------------------------------------------------------------------
Lab 10, Task 15
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-26
------------------------------------------------------------------------
"""
from functions import matrix_transpose, generate_matrix_num, print_matrix_num

ROWS = 4
COLS = 3
LOW = -10
HIGH = 10

matrix = generate_matrix_num(ROWS, COLS, LOW, HIGH, "int")
print("Original Matrix:")
print_matrix_num(matrix, "int")
print()
matrix_T = matrix_transpose(matrix)
print("Transposed Matrix:")
print_matrix_num(matrix_T, "int")
