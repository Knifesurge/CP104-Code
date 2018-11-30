"""
------------------------------------------------------------------------
Lab 9, Task 8
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-19
------------------------------------------------------------------------
"""
from functions import append_increment

file_handle = open('numbers.txt', 'r+')
print("file 'numbers.txt' open for reading and writing")
num = append_increment(file_handle)
file_handle.close()

print("{} is appended".format(num))
