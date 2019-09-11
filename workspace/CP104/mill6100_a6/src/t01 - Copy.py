"""
------------------------------------------------------------------------
Assignment 6, Task 1
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-03
------------------------------------------------------------------------
"""
from functions import get_brightness

wattage = int(input("Lightbulb wattage (w): "))

brightness = get_brightness(wattage)

if brightness != None:
    print("Brightness: {} lumens".format(brightness))
else:
    print("Invalid wattage")