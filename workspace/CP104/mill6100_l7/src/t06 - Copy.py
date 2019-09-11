"""
------------------------------------------------------------------------
Lab 7, Task 6
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-05
------------------------------------------------------------------------
"""
from functions import is_palindrome

string = input("Enter a string: ")

if is_palindrome(string):
    print("'{}' is a palindrome.".format(string))
else:
    print("'{}' is not a palindrome.".format(string))