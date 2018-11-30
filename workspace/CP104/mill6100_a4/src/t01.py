"""
------------------------------------------------------------------------
Assignment 4, Task 1
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-29
------------------------------------------------------------------------
"""
HOT_DAY = 28    # degrees Celsius or greater
PLEASANT_DAY = 18   # degrees Celsius, up to and including 27
COLD_DAY = 17   # degrees Celsius or lower


num_temps = 1
num_hot = 0
num_pleasant = 0
num_cold = 0
total = 0

temperature = int(input("Temperature C (-500 to stop): "))

while temperature != -500:
    total += temperature
    if temperature >= HOT_DAY:
        num_hot += 1
    elif temperature > PLEASANT_DAY:
        num_pleasant += 1
    elif temperature <= COLD_DAY:
        num_cold += 1
    num_temps += 1
    temperature = int(input("Temperature C (-500 to stop): "))
    
print("\nCold days:        {}".format(num_cold))
print("Pleasant days:    {}".format(num_pleasant))
print("Hot days:         {}".format(num_hot))
average = total / num_temps
print("Average:          {:.2f} C".format(average))