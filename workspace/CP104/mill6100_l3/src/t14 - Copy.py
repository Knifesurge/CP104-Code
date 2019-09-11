"""
------------------------------------------------------------------------
Lab 3, Task 14
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-20
------------------------------------------------------------------------
"""
richter_number = float(input("Richter Scale Number: "))
damage_scale = None

if richter_number < 5:
    damage_scale = "Little or no damage"
elif richter_number < 5.5:
    damage_scale = "Some damage"
elif richter_number < 6.5:
    damage_scale = "Serious damage: Walls may crack or fall"
elif richter_number < 7.5:
    damage_scale = "Disaster: Houses and buildings may collapse"
elif richter_number >= 7.5:
    damage_scale = "Catastrophe: Most buildings destroyed"
    
print("{}".format(damage_scale))