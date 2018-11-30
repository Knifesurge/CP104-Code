"""
------------------------------------------------------------------------
Lab 4, Task 6
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-28
------------------------------------------------------------------------
"""
value = float(input("First value: "))
total = 0
count = 1   # Defaults to 1 to avoid division by 0 if user enters 0 as first value

while value != 0:
    total += value
    value = float(input("Next value: "))
    count += 1
    
count -= 1  # Removes initial value of 1
    
print("Total: {:,.2f}".format(total))
average = total / count
print("Average: {:,.2f}".format(average))