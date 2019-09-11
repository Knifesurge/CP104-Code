"""
------------------------------------------------------------------------
Lab 3, Task 11
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-20
------------------------------------------------------------------------
"""
MAXIMUM_WIDTH = 2   # In barrels
width = height = None   # Declare and initialize
num_barrels = int(input("Number of barrels to bury: "))

if num_barrels < MAXIMUM_WIDTH:
    width = 1
    height = 1
elif num_barrels >= MAXIMUM_WIDTH:
    width = MAXIMUM_WIDTH
    height = num_barrels // MAXIMUM_WIDTH
    
print("The size of the pit is {} barrel(s) by {} barrel(s).".format(width, height))
    