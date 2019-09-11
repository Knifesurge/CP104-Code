"""
------------------------------------------------------------------------
Lab 3, Task 13
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-20
------------------------------------------------------------------------
"""
wind_category = None

wind_speed = int(input("Wind speed (km/h): "))

if wind_speed < 39:
    wind_category = "Breeze"
elif wind_speed < 61:
    wind_category = "Strong Wind"
elif wind_speed < 88:
    wind_category = "Gale Winds"
elif wind_speed < 117:
    wind_category = "Whole Gale"
elif wind_speed > 117:
    wind_category = "Hurricane"
    
print("Characterization: {}".format(wind_category))