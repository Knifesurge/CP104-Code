"""
------------------------------------------------------------------------
Lab 4, Task 7
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-28
------------------------------------------------------------------------
"""
minimum_value = 0
maximum_value = 0
value = float(input("First value: "))

while value != 0:
    if value > maximum_value:
        maximum_value = value
    elif value < minimum_value:
        minimum_value = value
    value = float(input("Next value: "))
    
print("Minimum: {:,.1f}".format(minimum_value))
print("Maximum: {:,.1f}".format(maximum_value))