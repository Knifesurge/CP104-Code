"""
------------------------------------------------------------------------
Lab 5, Task 2
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-10-15
------------------------------------------------------------------------
"""
number = int(input("Enter n: "))
total_sum = 0

for num in range(2, number, 2):
    total_sum += num

print("The sum of all even numbers from 2 to {} is: {}".format(number, total_sum))