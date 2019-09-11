"""
------------------------------------------------------------------------
Lab 3, Task 3
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-18
------------------------------------------------------------------------
"""
# Leap year defined as:
# - A year that is divisible by 4, but not by 100, unless divisible by 400
# Examples:
# NOT Leap Years: 1700, 1800, 1900
# ARE Leap Years: 1600, 2000

year = int(input("Enter a year (>0): "))

if (year % 100) == 0:
    if (year % 4) == 0:
        if (year % 400) == 0:
            leap_year = True
        else:
            leap_year = False
    else:
        leap_year = False
else:
    leap_year = False
    
if leap_year:
    print("{} is a leap year".format(year))
else:
    print("{} is not a leap year".format(year))
