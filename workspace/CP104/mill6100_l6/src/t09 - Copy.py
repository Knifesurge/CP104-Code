"""
------------------------------------------------------------------------
Lab 6, Task 9
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-10-29
------------------------------------------------------------------------
"""
from functions import is_divisible

number_to_check = int(input("Enter number to check for divisibility: "))
first_val = int(input("Enter first value to divide by: "))
second_val = int(input("Enter second value to divide by: "))

divisible = is_divisible(number_to_check, first_val, second_val)

if divisible:
    print("\n{} is evenly divisible by {} and {}".format(number_to_check, first_val, second_val))
else:
    print("\n{} is not evenly divisible by {} and {}".format(number_to_check, first_val, second_val))
        