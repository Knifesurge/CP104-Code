"""
------------------------------------------------------------------------
Assignment 8, Task 7
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-20
------------------------------------------------------------------------
"""
from functions import num_to_text

"""
num = int(input())

while num != 0:
    text = num_to_text(num)
    print("{} - {}".format(num, text))
    num = int(input())
"""

""" Generates list 1 -> 99 """
for i in range(1, 100):
    text = num_to_text(i)
    print("{} = {}".format(i, text))