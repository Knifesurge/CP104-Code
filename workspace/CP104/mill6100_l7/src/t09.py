"""
------------------------------------------------------------------------
Lab 7, Task 9
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-05
------------------------------------------------------------------------
"""
from functions import count_special_chars

string = input("Enter a string: ")

num_spec_chars = count_special_chars(string)

print("There are {} special characters.".format(num_spec_chars))