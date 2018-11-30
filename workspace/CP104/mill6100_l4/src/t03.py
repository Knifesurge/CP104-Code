"""
------------------------------------------------------------------------
Lab 4, Task 3
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-27
------------------------------------------------------------------------
"""
target_number = int(input("Enter target number: "))

nearest_power = 2

while nearest_power <= target_number:
    nearest_power *= 2
    
print("The nearest power of 2 >= {} is {}".format(target_number, nearest_power))