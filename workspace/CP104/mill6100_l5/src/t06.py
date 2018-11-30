"""
------------------------------------------------------------------------
Lab 5, Task 6
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-10-15
------------------------------------------------------------------------
"""
num_calories_burned_per_minute = float(input("Enter calories burned per minute: "))
minutes_beginning = int(input("Enter beginning number of minutes: "))
minutes_ending = int(input("Enter ending number of minutes: "))
minutes_increment = int(input("Enter the increment in minutes: "))

print()
for minute in range(minutes_beginning, minutes_ending + minutes_increment, minutes_increment):
    calories_burned = num_calories_burned_per_minute * minute
    print("Calories burned after {} minutes: {:.1f}".format(minute, calories_burned)) 