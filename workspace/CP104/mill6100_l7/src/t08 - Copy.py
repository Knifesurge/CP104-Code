"""
------------------------------------------------------------------------
Lab 7, Task 8
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-05
------------------------------------------------------------------------
"""
from functions import digit_count

string = input("Enter a string: ")

num_digits = digit_count(string)

print("There are {} digits.".format(num_digits))