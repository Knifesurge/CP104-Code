"""
------------------------------------------------------------------------
Lab 5, Task 15
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-10-15
------------------------------------------------------------------------
"""
base_minimum = int(input("Enter minimum value of base: "))
base_maximum = int(input("Enter maximum value of base: "))
base_increment = int(input("Enter increment in base value: "))
height_minimum = int(input("Enter minimum value of height: "))
height_maximum = int(input("Enter maximum value of height: "))
height_increment = int(input("Enter increment in height value: "))

print("\n\t\tCross-Sectional\tMoment of\tSection\nBase\tHeight\tArea\t\tInertia\t\tModulus")

for base in range(base_minimum, base_maximum + base_increment, base_increment):
    for height in range(height_minimum, height_maximum + height_increment, height_increment):
        cross_sectional_area = base * height
        moment_of_inertia = float((base * (height**3)) / 12)
        section_modulus = float((base * (height**2)) / 6)
        print("{:>4}\tx{:>5}\t{:>15.2f}\t{:>8.2f}\t{:>5.2f}".format(base, height, cross_sectional_area, moment_of_inertia, section_modulus))