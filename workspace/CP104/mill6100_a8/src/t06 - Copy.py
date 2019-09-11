"""
------------------------------------------------------------------------
Assignment 8, Task 6
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-22
------------------------------------------------------------------------
"""
from functions import categorize_accidents

city_accident_counts = [368, 200, 354, 234, 50, 23, 125, 99, 400, 389]

accidents = categorize_accidents(city_accident_counts)

print("City Accident Counts: {}".format(city_accident_counts))
print("Accidents Categorized: {}".format(accidents))

print("Category\tCounts")
print("< 100\t\t{}".format(accidents[0]))
print("< 200\t\t{}".format(accidents[1]))
print("< 300\t\t{}".format(accidents[2]))
print("< 400\t\t{}".format(accidents[3]))
print("400 or more\t{}".format(accidents[4]))