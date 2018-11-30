"""
------------------------------------------------------------------------
Lab 4, Task 9
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-28
------------------------------------------------------------------------
"""

""" Assumes end_celsius_temp > start_celsius_temp """

start_celsius_temp = int(input("Starting Celsius temperature: "))
end_celsius_temp = int(input("Ending Celsius temperature: "))

print("Celsius\tFahrenheit")
print("-----------------------")

for current_temp in range(start_celsius_temp, end_celsius_temp + 1): 
    fahrenheit = int((9 / 5) * current_temp + 32)
    print("{}\t{}".format(current_temp, fahrenheit))