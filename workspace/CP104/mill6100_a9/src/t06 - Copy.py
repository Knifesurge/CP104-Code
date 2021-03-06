"""
------------------------------------------------------------------------
Assignment 9, Task 6 - Substitute
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-28
------------------------------------------------------------------------
"""
from functions import substitute

filename_in = input("Input file: ")
filename_out = input("Output file: ")
ciphertext = input("Enter ciphertext: ")

fh_in = open(filename_in, "r")
fh_out = open(filename_out, "w")

substitute(fh_in, fh_out, ciphertext.upper())

fh_in.close()
fh_out.close()
print("Done")