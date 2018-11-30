"""
------------------------------------------------------------------------
Lab 9, Task 15
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-19
------------------------------------------------------------------------
"""
from functions import file_copy_n

file_handle_1 = open('words.txt', 'r')
file_handle_2 = open('new_words.txt', 'w')
print("Copying 'words.txt' to 'new_words.txt'")
n = int(input("Number of lines to copy: "))
file_copy_n(file_handle_1, file_handle_2, n)
file_handle_1.close()
file_handle_2.close()