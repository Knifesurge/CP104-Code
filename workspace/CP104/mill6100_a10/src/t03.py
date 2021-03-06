"""
------------------------------------------------------------------------
Assignment 10, Task 3 - Matrix Multiply
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-27
------------------------------------------------------------------------
"""
from functions import matrix_multiply, print_matrix_num, matrix_transpose

a = [[4, 5, 4], [5, 2, 2]]
b = [[5, 3], [0, 2], [1, 5]]

print("Matrix a:")
print_matrix_num(a, "int")
print("\nMatrix b:")
print_matrix_num(b, "int")

c = matrix_multiply(a, b)
print("\nMatrix c:")
print_matrix_num(c, "int")

print("\n-------------------------------")
print("Transposed Matrices:")

print("Matrix a:")
print_matrix_num(matrix_transpose(a), "int")
print("\nMatrix b:")
print_matrix_num(matrix_transpose(b), "int")
print("\nMatrix c:")
print_matrix_num(matrix_transpose(c), "int")