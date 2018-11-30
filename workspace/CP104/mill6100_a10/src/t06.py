"""
------------------------------------------------------------------------
Assignment 10, Task 6 - Grayscale
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-29
------------------------------------------------------------------------
"""
from functions import grayscale

fh_in = open("stupidColour.bmp", "rb")
fh_out = open("stupidColour_gray.bmp", "wb")

grayscale(fh_in, fh_out)

fh_in.close()
fh_out.close()