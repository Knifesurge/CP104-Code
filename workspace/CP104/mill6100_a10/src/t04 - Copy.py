"""
------------------------------------------------------------------------
Assignment 10, Task 4 - Pig Latin
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-27
------------------------------------------------------------------------
"""
from functions import pig_latin

while True:
    word = input("Word: ")
    pl = pig_latin(word)
    print("Pig Latin: {}".format(pl))
    print()