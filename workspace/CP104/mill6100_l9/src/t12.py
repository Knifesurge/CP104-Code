"""
------------------------------------------------------------------------
Lab 9, Task 12
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-19
------------------------------------------------------------------------
"""
from functions import find_shortest

file_handle = open('words.txt', 'r')
print("file 'words.txt' open for reading")
shortest = find_shortest(file_handle).strip()
file_handle.close()

print("'{}' is the first shortest word".format(shortest))