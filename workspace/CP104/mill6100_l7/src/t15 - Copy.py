"""
------------------------------------------------------------------------
Lab 7, Task 15
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-05
------------------------------------------------------------------------
"""
from functions import calculate

expr = input("Enter an expression: ")

result = calculate(expr)

print("{} = {}".format(expr, result))