"""
------------------------------------------------------------------------
Lab 2, Task 14
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-17
------------------------------------------------------------------------
"""
total_minutes = int(input("Enter number of minutes: "))
# There are 1440 minutes in a day, 24 hours in a day, 60 minutes in an hour
days = total_minutes // 1440
hours = int((total_minutes - (days * 1440)) / 60)
minutes = int((total_minutes - (hours * 60)) % 60)
print("There are {} days, {} hours, and {} minutes in {} minutes".format(days, hours, minutes, total_minutes))
