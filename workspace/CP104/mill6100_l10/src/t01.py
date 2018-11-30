"""
------------------------------------------------------------------------
Lab 10, Task 1
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-22
------------------------------------------------------------------------
"""
from functions import generate_matrix_num

rows = int(input("Number of rows: "))
cols = int(input("Number of cols: "))
low = int(input("Low value: "))
high = int(input("High value: "))
type = input("Type of values: ")

matrix = generate_matrix_num(rows, cols, low, high, type)

print(matrix)