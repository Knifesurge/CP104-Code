"""
------------------------------------------------------------------------
Assignment 9, Task 5 - Student Info
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-28
------------------------------------------------------------------------
"""
from functions import student_info

filename = input("Input file: ")

fh = open(filename, "r")

l_id, h_id, avg = student_info(fh)

fh.close()

print("ID of lowest mark: {}".format(l_id))
print("ID of highest mark: {}".format(h_id))
print("Average: {:.2f}".format(avg))