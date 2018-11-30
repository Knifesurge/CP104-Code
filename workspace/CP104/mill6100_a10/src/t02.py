"""
------------------------------------------------------------------------
Assignment 10, Task 2 - Flatten
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-27
------------------------------------------------------------------------
"""
from functions import flatten

# matrix = [[0, 1], [2, 3]]
matrix = [[7.11, 6.07, 1.94], [9.35, 6.76, 5.66], \
          [8.07, 7.3, 5.65], [3.84, 3.83, 8.46]]


print("Original: {}".format(matrix))
flattened = flatten(matrix)

print("Flattened: {}".format(flattened))