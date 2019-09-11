"""
------------------------------------------------------------------------
Lab 9, Task 6
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-19
------------------------------------------------------------------------
"""
from functions import number_stats

file_handle = open('numbers.txt', 'r')

smallest, largest, total, average = number_stats(file_handle)

print("Smallest: {}".format(smallest))
print("Largest: {}".format(largest))
print("Total: {}".format(total))
print("Average: {}".format(average))