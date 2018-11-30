"""
------------------------------------------------------------------------
Assignment 5, Task 1
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-10-23
------------------------------------------------------------------------
"""
GRAMS_PER_PENNYWEIGHT = 1.5552

print("Pennyweight to Grams Conversion")
start = int(input("Start: "))
limit = int(input("Limit: "))
increment = int(input("Increment: "))

print("{:>11s} {:>9s}".format("Pennyweight", "Grams"))
print("{:->11s} {:->9s}".format("",""))

for pennyweight in range(start, limit + increment, increment):
    grams = pennyweight * GRAMS_PER_PENNYWEIGHT
    print("{:>11d} {:>9.4f}".format(pennyweight, grams))