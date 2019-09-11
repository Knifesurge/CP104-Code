"""
------------------------------------------------------------------------
Lab 5, Task 3
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-10-15
------------------------------------------------------------------------
"""
n = int(input("Enter n: "))
total_sum = 0

for i in range(1, n + 1):
    total_sum += float(1 / i)
    
print("The sum of the series 1 to 1/{} is: {}".format(n, total_sum))
