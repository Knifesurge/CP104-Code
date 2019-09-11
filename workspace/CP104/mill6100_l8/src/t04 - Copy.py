"""
------------------------------------------------------------------------
Lab 8, Task 4
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-11
------------------------------------------------------------------------
"""
from functions import generate_integer_list

num_values = int(input("Number of values: "))
low_value = int(input("Low value: "))
high_value = int(input("High value: "))

values = generate_integer_list(num_values, low_value, high_value)

print("Values: {}".format(values))