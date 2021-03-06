"""
------------------------------------------------------------------------
Lab 9, Task 2
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-18
------------------------------------------------------------------------
"""
from functions import get_customer_by_id

print("Find customer by id number")

customer_id = input("Enter an ID: ")

file_handle = open('customers.txt', 'r')
customer = get_customer_by_id(file_handle, customer_id)
file_handle.close()

print(customer)