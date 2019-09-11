"""
------------------------------------------------------------------------
Lab 9, Task 13
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-19
------------------------------------------------------------------------
"""
from functions import delete_line

file_handle = open('words.txt', 'r+')
print("file 'words.txt' open for reading/writing")
line_num = int(input("Enter line number to delete: "))
removed = delete_line(file_handle, line_num) 
file_handle.close()

print("Line {} deleted:".format(line_num))
print(removed)