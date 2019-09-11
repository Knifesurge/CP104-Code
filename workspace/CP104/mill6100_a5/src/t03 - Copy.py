"""
------------------------------------------------------------------------
Assignment 5, Task 3
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-01
------------------------------------------------------------------------
"""
num = int(input("Number (>=1): "))
total = 0

for n in range(1, num + 1):
    total += (1 / (n ** 2))
    
print("Sum of inverse squares for {} = {}".format(num, total))