"""
------------------------------------------------------------------------
Lab 10, Task 8
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-26
------------------------------------------------------------------------
"""
from functions import find_position, generate_matrix_num, print_matrix_num

rows = int(input("Number of rows: "))
cols = int(input("Number of cols: "))
low = int(input("Low value: "))
high = int(input("High value: "))

matrix = generate_matrix_num(rows, cols, low, high, "int")

print_matrix_num(matrix, "int")

s_loc, l_loc = find_position(matrix)

print("\nSmallest position: {}".format(s_loc))
print("Smallest value: {}".format(matrix[s_loc[0]][s_loc[1]]))
print("Largest position: {}".format(l_loc))
print("Largest value: {}".format(matrix[l_loc[0]][l_loc[1]]))