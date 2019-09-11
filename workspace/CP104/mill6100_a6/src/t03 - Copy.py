"""
------------------------------------------------------------------------
Assignment 6, Task 3
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-05
------------------------------------------------------------------------
"""
from functions import get_total_change

nickels = int(input("Enter number of nickels: "))
dimes = int(input("Enter number of dimes: "))
quarters = int(input("Enter number of quarters: "))
loonies = int(input("Enter number of loonies: "))
toonies = int(input("Enter number of toonies: "))

total = get_total_change(nickels, dimes, quarters, loonies, toonies)

print("Total: ${:,.2f}".format(total))