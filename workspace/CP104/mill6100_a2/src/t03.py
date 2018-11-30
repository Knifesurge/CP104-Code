"""
------------------------------------------------------------------------
Assignment 2, Task 3
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-17
------------------------------------------------------------------------
"""
large_dog_cost = 75.00
small_dog_cost = 50.00

num_large_dogs_groomed = int(input("Number of large dogs groomed: "))
num_small_dogs_groomed = int(input("Number of small dogs groomed: "))

total_earned = (num_large_dogs_groomed * large_dog_cost) + (num_small_dogs_groomed * small_dog_cost)

print("Total earned for the day: ${:,.2f}".format(total_earned))