"""
------------------------------------------------------------------------
Lab 10, Task 2
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-22
------------------------------------------------------------------------
"""
from functions import generate_matrix_char

rows = int(input("Number of rows: "))
cols = int(input("Number of cols: "))

matrix = generate_matrix_char(rows, cols)

print(matrix)