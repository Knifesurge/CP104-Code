"""
------------------------------------------------------------------------
Assignment 10, Task 5 - Cereals
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-27
------------------------------------------------------------------------
"""
from functions import read_cereals, cereals_by_value, cereal_stats, cereal_stats_table

fh = open('cereals.txt', 'r')
cereals = read_cereals(fh)
print(cereals)

column = input("Column: ")
value = input("Value: ")

some_cereals = cereals_by_value(cereals, column, value)

for row in some_cereals:
    print(row)
    
columns = ["calories", "protein", "sugar"]

data = cereal_stats(cereals, columns)

print("Raw data:\n{}".format(data))
print("\n")

cereal_stats_table(data)
