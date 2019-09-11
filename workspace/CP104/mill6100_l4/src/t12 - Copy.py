"""
------------------------------------------------------------------------
Lab 4, Task 12
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-28
------------------------------------------------------------------------
"""
min_value = int(input("Enter the min value: "))
max_value = int(input("Enter the max value: "))

value = int(input("Enter an integer {} <= n <= {}: ".format(min_value, max_value)))

while value not in range(min_value, max_value + 1):
    print("Bad value!")
    value = int(input("Enter an integer {} <= n <= {}: ".format(min_value, max_value)))

print("You entered: {}".format(value))