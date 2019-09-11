"""
------------------------------------------------------------------------
Assignment 6, Task 5
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-05
------------------------------------------------------------------------
"""
from functions import time_values

seconds = int(input("Number of seconds: "))

days, hours, minutes = time_values(seconds)

print("{} seconds is the same as: ".format(seconds))
print("{:>2} days".format(days))
print("{:>2} hours".format(hours))
print("{:>2} minutes".format(minutes))