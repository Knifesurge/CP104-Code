"""
------------------------------------------------------------------------
Lab 8, Task 7
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-11
------------------------------------------------------------------------
"""
from functions import list_categorize, generate_integer_list
from random import randint

NUM_VALUES = randint(1, 15)
LOW_VALUE = -100
HIGH_VALUE = 100

values = generate_integer_list(NUM_VALUES, LOW_VALUE, HIGH_VALUE)

print("Values: {}".format(values))

negatives, positives, zeroes, evens, odds = list_categorize(values)

print("Negatives: {}".format(negatives))
print("Positives: {}".format(positives))
print("Zeroes: {}".format(zeroes))
print("Evens: {}".format(evens))
print("Odds: {}".format(odds))