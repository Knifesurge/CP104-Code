"""
------------------------------------------------------------------------
Lab 7, Task 1
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-04
------------------------------------------------------------------------
"""
from functions import is_hydroxide

chemical = input("Enter a chemical formula: ")

if is_hydroxide(chemical):
    print("{} is a hydroxide.".format(chemical))
else:
    print("{} is not a hydroxide.".format(chemical))
