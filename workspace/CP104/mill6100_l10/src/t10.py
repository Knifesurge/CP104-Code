"""
------------------------------------------------------------------------
Lab 10, Task 10
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-26
------------------------------------------------------------------------
"""
from functions import count_frequency, generate_matrix_char, print_matrix_char

rows = int(input("Number of rows: "))
cols = int(input("Number of cols: "))

matrix = generate_matrix_char(rows, cols)

print_matrix_char(matrix)
print()

c = input("Enter the character to search for: ")

count = count_frequency(matrix, c)

print("Character {} appears {} times in the matrix.".format(c, count))