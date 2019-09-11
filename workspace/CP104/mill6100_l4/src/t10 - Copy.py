"""
------------------------------------------------------------------------
Lab 4, Task 10
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-28
------------------------------------------------------------------------
"""

""" Assumes end_fahrenheit_temp > start_fahrenheit_temp """

start_fahrenheit_temp = int(input("Starting Fahrenheit temperature: "))
end_fahrenheit_temp = int(input("Ending Fahrenheit temperature: "))

print("Fahrenheit\tCelsius")
print("-----------------------")

for current_temp in range(start_fahrenheit_temp, end_fahrenheit_temp + 1): 
    celsius = int((5 / 9) * (current_temp - 32))
    print("{}\t{}".format(current_temp, celsius))