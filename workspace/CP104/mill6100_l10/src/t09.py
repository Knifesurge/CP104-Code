"""
------------------------------------------------------------------------
Lab 10, Task 9
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-26
------------------------------------------------------------------------
"""
from functions import find_less, generate_matrix_num, print_matrix_num

rows = int(input("Number of rows: "))
cols = int(input("Number of cols: "))
low = int(input("Low value: "))
high = int(input("High value: "))
n = int(input("Number to find: "))

matrix = generate_matrix_num(rows, cols, low, high, "int")

print_matrix_num(matrix, "int")

loc = find_less(matrix, n)
x = loc[0]
y = loc[1]
value = matrix[x][y]

print("\nPosition: {}".format(loc))
print("Value: {}".format(value))