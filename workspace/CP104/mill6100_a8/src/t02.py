"""
------------------------------------------------------------------------
Assignment 8, Task 2
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-20
------------------------------------------------------------------------
"""
from functions import clean_list
from random import randrange

values = []

for i in range(20):
    values.append(randrange(10))
    
clean_list(values)

print("Values: {}".format(values))
print("Cleaned: {}".format(values))