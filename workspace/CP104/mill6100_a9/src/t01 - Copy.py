"""
------------------------------------------------------------------------
Assignment 9, Task 1 - File Head
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-27
------------------------------------------------------------------------
"""
from functions import file_head

file_name = input("Enter input file name: ")

fh = open(file_name, "r")

n = int(input("Enter n: "))

file_head(fh, n)
fh.close()