"""
------------------------------------------------------------------------
Lab 4, Task 8
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-28
------------------------------------------------------------------------
"""
num_negatives = 0
num_positives = 0

value = float(input("First value: "))

while value != 0:
    if value < 0:
        num_negatives += 1
    elif value > 0:
        num_positives += 1
    value = float(input("Next value: "))
    
print("Number of positive values: {}".format(num_positives))
print("Number of negative values: {}".format(num_negatives))