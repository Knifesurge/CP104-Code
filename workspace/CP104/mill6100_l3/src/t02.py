"""
------------------------------------------------------------------------
Lab 3, Task 2
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-18
------------------------------------------------------------------------
"""
target = float(input("Enter target: "))
v1 = float(input("Enter v1: "))
v2 = float(input("Enter v2: "))
abs_v1 = abs(v1)    # Absolute value of v1. Used for calculation purposes
abs_v2 = abs(v2)    # Absolute value of v2. Used for calculation purposes

# Distance b/w target and v1 is greater than distance b/w target and v2
if abs_v1 == abs_v2:
    closest_value = v1
elif (abs(target - abs_v1)) > (abs(target - abs_v2)):
    closest_value = v2
else:
    closest_value = v1
    
print("Closest value to {} is {}".format(target, closest_value))
