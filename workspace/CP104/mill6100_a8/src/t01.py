"""
------------------------------------------------------------------------
Assignment 8, Task 1
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-20
------------------------------------------------------------------------
"""
from functions import bag_to_set
from random import randrange

bag = []

for i in range(10):
    bag.append(randrange(10))

set = bag_to_set(bag)

print("Bag: {}".format(bag)) 
print("Set: {}".format(set))