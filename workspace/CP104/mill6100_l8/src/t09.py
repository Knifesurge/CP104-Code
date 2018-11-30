"""
------------------------------------------------------------------------
Lab 8, Task 9
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-12
------------------------------------------------------------------------
"""
from functions import many_search, generate_integer_list
from random import randint

NUM_VALUES = randint(1, 15)
LOW_VALUE = -100
HIGH_VALUE = 100

values = generate_integer_list(NUM_VALUES, LOW_VALUE, HIGH_VALUE)

print("Values: {}".format(values))

for i in range(3):
    val = int(input("Enter a value: "))
    indexes = many_search(values, val)
    print("Indexes of {}: {}".format(val, indexes))
