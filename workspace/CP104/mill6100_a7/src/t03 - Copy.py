"""
------------------------------------------------------------------------
Assignment 7, Task 3
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-16
------------------------------------------------------------------------
"""
from functions import my_find

string = input("String to search: ")
search_for = input("String to search for: ")

index = my_find(string, search_for)

print("'{}' is found at location {} in '{}'".format(search_for, index, string))
