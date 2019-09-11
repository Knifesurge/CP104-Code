"""
------------------------------------------------------------------------
Lab 8, Task 5
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-11
------------------------------------------------------------------------
"""
from functions import get_lotto_numbers

num_values = int(input("Number of values: "))
low_value = int(input("Low value: "))
high_value = int(input("High value: "))

lotto_numbers = get_lotto_numbers(num_values, low_value, high_value)

print("Lotto Numbers: {}".format(lotto_numbers))