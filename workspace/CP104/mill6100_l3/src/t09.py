"""
------------------------------------------------------------------------
Lab 3, Task 9
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-20
------------------------------------------------------------------------
"""
print("For rectangle 1:")
rect1_length = float(input("Length of rectangle (cm): "))
rect1_width = float(input("Width of rectangle (cm): "))
print("For rectangle 2:")
rect2_length = float(input("Length of rectangle (cm): "))
rect2_width = float(input("Width of rectangle (cm): "))

rect1_area = rect1_length * rect1_width
rect2_area = rect2_length * rect2_width

print("Area of rectangle 1: {:.1f} cm^2".format(rect1_area))
print("Area of rectangle 2: {:.1f} cm^2".format(rect2_area))

if rect1_area > rect2_area:
    print("Area of rectangle 1 is greater than area of rectangle 2.")
elif rect1_area < rect2_area:
    print("Area of rectangle 1 is less than area of rectangle2.")
else:
    print("The two areas are equal")