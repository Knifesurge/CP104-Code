"""
------------------------------------------------------------------------
Assignment 9, Task 2 - Number Lines
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-27
------------------------------------------------------------------------
"""
from functions import number_lines

filename_in = input("Enter input file name: ")
filename_out = input("Enter output file name: ")

fh_in = open(filename_in, "r")
fh_out = open(filename_out, "w")

number_lines(fh_in, fh_out)

fh_in.close()
fh_out.close()