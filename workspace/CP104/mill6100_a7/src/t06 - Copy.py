"""
------------------------------------------------------------------------
Assignment 7, Task 6
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-15
------------------------------------------------------------------------
"""
from functions import number_convert

number = input("Enter phone number: ")

converted = number_convert(number)

print("Digits: {}".format(converted))