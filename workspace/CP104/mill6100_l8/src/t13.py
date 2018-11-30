"""
------------------------------------------------------------------------
Lab 8, Task 13
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-12
------------------------------------------------------------------------
"""
from functions import union, generate_integer_list
from random import randint

NUM_VALUES = randint(1, 9)
LOW_VALUE = 0
HIGH_VALUE = 100

values1 = generate_integer_list(NUM_VALUES, LOW_VALUE, HIGH_VALUE)
values2 = generate_integer_list(NUM_VALUES, LOW_VALUE, HIGH_VALUE)

print("Values 1: {}".format(values1))
print("Values 2: {}".format(values2))

list_union = union(values1, values2) 
print("Totals: {}".format(list_union))