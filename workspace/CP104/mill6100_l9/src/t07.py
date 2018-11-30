"""
------------------------------------------------------------------------
Lab 9, Task 7
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-19
------------------------------------------------------------------------
"""
from functions import append_max_num

file_handle = open('numbers.txt', 'r+')
print("file 'numbers.txt' open for reading and writing")
max_num = append_max_num(file_handle)
file_handle.close()

print("{} is appended".format(max_num))
