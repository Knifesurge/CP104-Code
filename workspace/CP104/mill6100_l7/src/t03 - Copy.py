"""
------------------------------------------------------------------------
Lab 7, Task 3
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-05
------------------------------------------------------------------------
"""
from functions import parse_code

product_code = input("Enter a product code: ")

pc, pi, pq = parse_code(product_code)

print("Category:\t{}".format(pc))
print("ID:\t\t{}".format(pi))
print("Qualifier:\t{}".format(pq))