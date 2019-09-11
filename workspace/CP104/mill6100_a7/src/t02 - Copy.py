"""
------------------------------------------------------------------------
Assignment 7, Task 2
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-14
------------------------------------------------------------------------
"""
from functions import my_isalpha

test_string = input("Enter a string to test: ")

all_alpha = my_isalpha(test_string)

if all_alpha:
    print("The string is all letters")
else:
    print("The string contains non-letters")