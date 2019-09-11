"""
------------------------------------------------------------------------
Lab 7, Task 2
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-05
------------------------------------------------------------------------
"""
from functions import url_categorize

url = input("Enter the website address: ")

type = url_categorize(url)

print(type)