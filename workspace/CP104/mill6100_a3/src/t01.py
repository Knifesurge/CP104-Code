"""
------------------------------------------------------------------------
Assignment 3, Task 1
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-20
------------------------------------------------------------------------
"""
num_balloons = int(input("Balloons collected: "))
bonus_points = 0 # Defaults to 0

if num_balloons == 1:
    bonus_points = 10
elif num_balloons == 2:
    bonus_points = 25
elif num_balloons >= 3:
    bonus_points = 50
    
print("Bonus points earned: {}".format(bonus_points))