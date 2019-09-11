"""
------------------------------------------------------------------------
Lab 6, Task 3
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-10-29
------------------------------------------------------------------------
"""
from functions import sum_partial_harmonic

n = int(input("Enter n: "))

total = sum_partial_harmonic(n)

print("The sum of the series 1 to 1/{} is: {}".format(n, total))