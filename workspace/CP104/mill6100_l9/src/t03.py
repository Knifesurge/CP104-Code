"""
------------------------------------------------------------------------
Lab 9, Task 3
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-18
------------------------------------------------------------------------
"""
from functions import get_best_customer

print("Find customer with largest balance:")

file_handle = open('customers.txt', 'r')
best_customer = get_best_customer(file_handle)
file_handle.close()

print(best_customer)