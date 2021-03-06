"""
------------------------------------------------------------------------
Assignment 9, Task 3 - Get Addresses
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-27
------------------------------------------------------------------------
"""
from functions import get_addresses

filename = input("Enter address file name: ")

fh = open(filename, "r")

addresses = get_addresses(fh)

fh.close()

for address in addresses:
    print(address)
