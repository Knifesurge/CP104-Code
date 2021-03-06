"""
------------------------------------------------------------------------
Assigment 10, Task 1 - Binary Search
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-27
------------------------------------------------------------------------
"""
from functions import binary_search
from random import randint

values = []
VALUES_LENGTH = 10
for i in range(VALUES_LENGTH):
    values.append(randint(0, 101))

print("Search: {} ".format(values), end='')
search = int(input("for: "))

index = binary_search(values, search)
print("Index: {}".format(index))