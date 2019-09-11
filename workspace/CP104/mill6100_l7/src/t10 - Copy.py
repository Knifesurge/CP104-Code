"""
------------------------------------------------------------------------
Lab 7, Task 10
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-05
------------------------------------------------------------------------
"""
from functions import text_analyze

txt = input("Enter a string: ")

uppr, lowr, dgts, whtspc = text_analyze(txt)

print("Upper case letters: {}".format(uppr))
print("Lower case letters: {}".format(lowr))
print("Digits: {}".format(dgts))
print("Whitespace characters: {}".format(whtspc))