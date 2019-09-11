"""
------------------------------------------------------------------------
Lab 3, Task 10
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-20
------------------------------------------------------------------------
"""
GRAVITY_ACCEL = 9.8 # m/s^2

mass = float(input("Enter mass (kg): "))

weight = mass * GRAVITY_ACCEL   # N (Newtons)

print("Weight: {:.1f} N".format(weight))

if weight > 1000:
    print("Object is too heavy.")
elif weight < 10:
    print("Object is too light.")