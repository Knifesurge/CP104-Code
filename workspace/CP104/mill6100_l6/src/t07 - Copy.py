"""
------------------------------------------------------------------------
Lab 6, Task 7
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-10-29
------------------------------------------------------------------------
"""
from functions import diameter, circumference, area

radius = float(input("Enter radius: "))

diameter = diameter(radius)
circumference = circumference(radius)
area = area(radius)

print("Diameter of circle: {:.2f}".format(diameter))
print("Circumference of circle: {:.2f}".format(circumference))
print("Area of circle: {:.2f}".format(area))