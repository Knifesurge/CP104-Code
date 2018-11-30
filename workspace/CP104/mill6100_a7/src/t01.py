"""
------------------------------------------------------------------------
Assignment 7, Task 1
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-14
------------------------------------------------------------------------
"""
from functions import my_isdigit

test_string = input("Enter a string to test: ")

all_digits = my_isdigit(test_string)

if all_digits:
    print("The string is all digits")
else:
    print("The string contains non-digits")