"""
------------------------------------------------------------------------
Lab 9, Task 4
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-19
------------------------------------------------------------------------
"""
from functions import get_first_customer

print("Find customer with earliest sign-in:")

file_handle = open('customers.txt', 'r')
first_customer = get_first_customer(file_handle)
file_handle.close()

print(first_customer)