"""
------------------------------------------------------------------------
Lab 7, Task 7
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-05
------------------------------------------------------------------------
"""
from functions import vowel_count

string = input("Enter a string: ")

vowels = vowel_count(string)

print("There are {} vowels.".format(vowels))