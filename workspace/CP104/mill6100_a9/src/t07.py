"""
------------------------------------------------------------------------
Assignment 9, Task 7 - Shift
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-28
------------------------------------------------------------------------
"""
from functions import shift

filename_in = input("Input file: ")
filename_out = input("Output file: ")
n = int(input("Enter shift: "))

fh_in = open(filename_in, "r")
fh_out = open(filename_out, "w")

shift(fh_in, fh_out, n)

fh_in.close()
fh_out.close()

print("Done")