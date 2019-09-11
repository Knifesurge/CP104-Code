"""
------------------------------------------------------------------------
Assignment 2, Task 6
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-17
------------------------------------------------------------------------
"""
num_flyers = int(input("Number of flyers: "))
num_volunteers = int(input("Number of volunteers: "))

flyers_per_volunteer = int(num_flyers // num_volunteers)
leftover_flyers = int(num_flyers - (num_volunteers * flyers_per_volunteer))

print("Flyers per volunteer: {:,d}".format(flyers_per_volunteer))
print("Flyers left over: {:,d}".format(leftover_flyers))