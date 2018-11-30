"""
------------------------------------------------------------------------
Lab 9, Task 1
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-18
------------------------------------------------------------------------
"""
from functions import get_customer_record

print("Find record n")

record_number = int(input("Enter a record number: "))

file_handle = open('customers.txt', 'r')
record = get_customer_record(file_handle, record_number)
file_handle.close()

print(record)