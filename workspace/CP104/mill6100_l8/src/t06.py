"""
------------------------------------------------------------------------
Lab 8, Task 6
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-11
------------------------------------------------------------------------
"""
from functions import list_stats, generate_integer_list
from random import randint

num_values = randint(1, 10)
low_value = -100
high_value = 100

values = generate_integer_list(num_values, low_value, high_value)

print("Values: {}".format(values))

smallest_value, largest_value, total, average = list_stats(values)

print("Smallest value: {}".format(smallest_value))
print("Largest value: {}".format(largest_value))
print("Total: {}".format(total))
print("Average: {}".format(average))
