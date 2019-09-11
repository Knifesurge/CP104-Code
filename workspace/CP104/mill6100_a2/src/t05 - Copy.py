"""
------------------------------------------------------------------------
Assignment 2, Task 5
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-17
------------------------------------------------------------------------
"""
PI = 3.14
diameter_of_base = float(input("Diameter of container base (cm): "))
height_of_container = float(input("Height of container (cm): "))
material_cost = float(input("Cost of material ($/cm^2): "))
num_containers = int(input("Number of containers: "))
radius_of_base = diameter_of_base / 2

area_of_base = PI * radius_of_base**2
area_of_outside = (PI * diameter_of_base) * height_of_container
surface_area = area_of_base + area_of_outside

single_cost = surface_area * material_cost
total_cost = single_cost * num_containers

print("The cost of one container is: ${:,.2f}".format(single_cost))
print("The cost of all containers is ${:,.2f}".format(total_cost))