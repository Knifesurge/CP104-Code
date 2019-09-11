"""
------------------------------------------------------------------------
Lab 8, Task 11
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-12
------------------------------------------------------------------------
"""
from functions import dot_product, generate_integer_list
from random import randint

NUM_VALUES = randint(1, 5)
LOW_VALUE = 0
HIGH_VALUE = 20

values1 = generate_integer_list(NUM_VALUES, LOW_VALUE, HIGH_VALUE)
values2 = generate_integer_list(NUM_VALUES, LOW_VALUE, HIGH_VALUE)

print("Values 1: {}".format(values1))
print("Values 2: {}".format(values2))

product = dot_product(values1, values2)

print("\nDot Product: {}".format(product))
