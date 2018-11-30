"""
------------------------------------------------------------------------
Lab 6, Task 13
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-10-29
------------------------------------------------------------------------
"""
from functions import square_pyramid

base = float(input("Length of base: "))
height = float(input("Perpendicular height of pyramid: "))

slant_height, area, volume = square_pyramid(base, height)

print("\nSlant height of square pyramid: {:.2f}".format(slant_height))
print("Area of square pyramid: {:.2f}".format(area))
print("Volume of square pyramid: {:.2f}".format(volume))