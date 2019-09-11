"""
------------------------------------------------------------------------
Assignment 7, Task 5
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-15
------------------------------------------------------------------------
"""
from functions import is_valid_isbn
isbn = input("Enter an ISBN to test: ")

valid_isbn = is_valid_isbn(isbn)

if valid_isbn:
    print("ISBN {} is valid".format(isbn))
else:
    print("ISBN {} is NOT valid".format(isbn))