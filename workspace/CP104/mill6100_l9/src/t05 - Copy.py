"""
------------------------------------------------------------------------
Lab 9, Task 5
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-19
------------------------------------------------------------------------
"""
from functions import append_customer

data = ["94563","Nick","Mills",945.63,"1999-03-25"]
file_handle = open('customers.txt', 'a')
append_customer(file_handle, data)
file_handle.close()

print("Data: {}".format(data))

print("data appended to file")
