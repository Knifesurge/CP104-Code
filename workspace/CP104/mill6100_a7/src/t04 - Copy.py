"""
------------------------------------------------------------------------
Assignment 7, Task 4
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-14
------------------------------------------------------------------------
"""
from functions import common_ending

s1 = input("First string: ")
s2 = input("Second string: ")

common = common_ending(s1, s2)

print("Common ending: {}".format(common))