"""
------------------------------------------------------------------------
Lab 8, Task 15
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-12
------------------------------------------------------------------------
"""
from functions import symmetric_difference, generate_integer_list
from random import randint

NUM_VALUES = randint(1, 9)
LOW_VALUE = 0
HIGH_VALUE = 100

#values1 = generate_integer_list(NUM_VALUES, LOW_VALUE, HIGH_VALUE)
#values2 = generate_integer_list(NUM_VALUES, LOW_VALUE, HIGH_VALUE)

values1 = [10, 3, 10, 3, 1]
values2 = [8, 2, 7, 3, 6, 10, 32, 99]

print("Values 1: {}".format(values1))
print("Values 2: {}".format(values2))

list_intersection = symmetric_difference(values1, values2) 
print("Totals: {}".format(list_intersection))