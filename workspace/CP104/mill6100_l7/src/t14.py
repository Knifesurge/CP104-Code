"""
------------------------------------------------------------------------
Lab 7, Task 14
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-05
------------------------------------------------------------------------
"""
from functions import str_distance

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

distance = str_distance(s1, s2)

print("Distance: {}".format(distance))