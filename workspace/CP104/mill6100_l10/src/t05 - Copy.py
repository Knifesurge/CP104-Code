"""
------------------------------------------------------------------------
Lab 10, Task 5
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-26
------------------------------------------------------------------------
"""
from functions import print_matrix_char, generate_matrix_char

rows = int(input("Number of rows: "))
cols = int(input("Number of cols: "))

matrix = generate_matrix_char(rows, cols)

print_matrix_char(matrix)