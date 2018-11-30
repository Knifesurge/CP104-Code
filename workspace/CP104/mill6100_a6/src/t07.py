"""
------------------------------------------------------------------------
Assignment 6, Task 7
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-05
------------------------------------------------------------------------
"""
from functions import wall_area, paint_required, hours_required, paint_cost

print("Enter paint and labour standards:")
standard_wall_area = int(input("Standard wall area (sq ft / gallon): "))
area_per_hour = int(input("Area painted per hour (sq ft / hour): "))
labour_charges = float(input("Labour charges ($ / hour): "))

print("\nEnter customer information:")
cost_of_paint = float(input("Cost of paint (1 gallon): $"))
height = int(input("Height of wall (ft): "))
width = int(input("Width of wall (ft): "))

area = wall_area(width, height)

required_paint = paint_required(area, standard_wall_area)
required_hours = hours_required(area, area_per_hour)
total_paint_cost = paint_cost(required_paint, cost_of_paint)
labour_cost = required_hours * labour_charges

print("\nPaint required: {:.0f} gallons".format(required_paint))
print("Hours labour required: {:.0f} hours".format(required_hours))
print("Paint cost:\t${:>9.2f}".format(total_paint_cost))
print("Labour cost:\t${:>9.2f}".format(labour_cost))