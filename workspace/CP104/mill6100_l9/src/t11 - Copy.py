"""
------------------------------------------------------------------------
Lab 9, Task 11
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-19
------------------------------------------------------------------------
"""
from functions import find_longest

file_handle = open('words.txt', 'r')
print("file 'words.txt' open for reading")
longest = find_longest(file_handle).strip()
file_handle.close()

print("'{}' is the last longest word".format(longest))