"""
------------------------------------------------------------------------
Assignment 6, Task 6
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-05
------------------------------------------------------------------------
"""
from functions import time_split

initial_seconds = int(input("Number of seconds: "))

days, hours, minutes, seconds = time_split(initial_seconds)

print("Days: {}, Hours: {}, Minutes: {}, Seconds: {}".format(days, hours, minutes, seconds))
