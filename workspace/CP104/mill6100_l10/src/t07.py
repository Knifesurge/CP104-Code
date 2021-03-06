"""
------------------------------------------------------------------------
Lab 10, Task 7
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-26
------------------------------------------------------------------------
"""
from functions import stats, generate_matrix_num, print_matrix_num

rows = int(input("Number of rows: "))
cols = int(input("Number of cols: "))
low = int(input("Low value: "))
high = int(input("High value: "))

matrix = generate_matrix_num(rows, cols, low, high, "int")

print_matrix_num(matrix, "int")

smallest, largest, total, average = stats(matrix)

print("\nSmallest: {}".format(smallest))
print("Largest: {}".format(largest))
print("Total: {}".format(total))
print("Average: {:.2f}".format(average))