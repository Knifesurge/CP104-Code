"""
------------------------------------------------------------------------
Assignment 3, Task 2
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-21
------------------------------------------------------------------------
"""
wattage = int(input("Lightbulb wattage (w): "))
brightness = "Invalid Wattage"  # Defaults to invalid wattage entered

if wattage == 15:
    brightness = "125"
elif wattage == 25:
    brightness = "215"
elif wattage == 40:
    brightness = "500"
elif wattage == 60:
    brightness = "880"
elif wattage == 75:
    brightness = "1000"
elif wattage == 100:
    brightness = "1675"
else:
    print(brightness)
    exit()  # To prevent following print statement from executing

print("Brightness: {} lumens".format(brightness))