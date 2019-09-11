"""
------------------------------------------------------------------------
Assignment 4, Task 2
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-29
------------------------------------------------------------------------
"""
current_population = int(input("Current Population: "))
growth_rate = (int(input("Growth Rate (%): "))) / 100
target_population = int(input("Target Population: "))

years = 0

intermediate_population = current_population + (current_population * growth_rate)

while intermediate_population < target_population:
    years += 1
    intermediate_population += (intermediate_population * growth_rate)
years += 1
print("It will take {} year(s) to reach the target population.".format(years))