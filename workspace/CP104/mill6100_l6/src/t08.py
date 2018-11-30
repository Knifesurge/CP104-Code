"""
------------------------------------------------------------------------
Lab 6, Task 8
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-10-29
------------------------------------------------------------------------
"""
from functions import is_leap

year = int(input("Enter a year (>0): "))

leap = is_leap(year)

if leap:
    print("{} is a leap year".format(year))
else:
    print("{} is not a leap year".format(year))
