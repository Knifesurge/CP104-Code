"""
------------------------------------------------------------------------
Lab 4, Task 15
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-29
------------------------------------------------------------------------
"""
minimum = 0
maximum = 0
total = 0
average = 0
count = 0

value = float(input("Enter first value: "))

while value != 0:
    count += 1
    if value < minimum:
        minimum = value
    elif value > maximum:
        maximum = value
    total += value
    value = float(input("Enter next value: "))
    
print("\nMinimum: {:,.2f}".format(minimum))
print("Maximum: {:,.2f}".format(maximum))
print("Total: {:,.2f}".format(total))
average = total / count
print("Average: {:,.2f}".format(average))