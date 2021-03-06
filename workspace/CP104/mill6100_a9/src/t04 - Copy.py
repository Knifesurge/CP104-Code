"""
------------------------------------------------------------------------
Assignment 9, Task 4 - Merge Letters
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-27
------------------------------------------------------------------------
"""
from functions import merge_letters

fh_letter = open("letter.txt", "r")
fh_addresses = open("addresses.txt", "r")
fh_merged = open("letter_merged.txt", "w")

merge_letters(fh_letter, fh_addresses, fh_merged)

fh_letter.close()
fh_addresses.close()
fh_merged.close()