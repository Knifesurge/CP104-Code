"""
------------------------------------------------------------------------
Lab 3, Task 15
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-20
------------------------------------------------------------------------
"""
x_coord = float(input("Enter the x coordinate: "))
y_coord = float(input("Enter the y coordinate: "))
quadrant = None

if x_coord > 0: # Left of origin (pos.)
    if y_coord > 0: # Above x-axis (pos.)
        quadrant = "quadrant 1"
    elif y_coord < 0:   # Below x-axis (neg.)
        quadrant = "quadrant 4"
    else:   # y-coord = 0
        quadrant = "x-axis"
elif x_coord < 0:   # Right of origin (neg.)
    if y_coord > 0: # Above x-axis (pos.)
        quadrant = "quadrant 2"
    elif y_coord < 0:   # Below x-axis (neg.)
        quadrant = "quadrant 3"
    else:   # y-coord = 0
        quadrant = "x-axis"
elif x_coord == 0:  # On origin OR on y-axis
    if y_coord == 0:
        quadrant = "origin"
    else:
        quadrant = "y-axis"
        
print("({:.2f},{:.2f}) is in/on the {}".format(x_coord, y_coord, quadrant))