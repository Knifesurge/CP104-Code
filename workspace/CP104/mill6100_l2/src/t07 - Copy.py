"""
------------------------------------------------------------------------
Lab 2, Task 7
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-17
------------------------------------------------------------------------
"""
breakfast = 6.75
lunch = 19.34
supper = 112.81

total = breakfast + lunch + supper

print("Meal", "{:>12s}".format("Cost"))
print("Breakfast    ${:.2f}".format(breakfast))
print("Lunch        ${:.2f}".format(lunch))
print("Supper       ${:.2f}".format(supper))
print("Total        ${:.2f}".format(total))
