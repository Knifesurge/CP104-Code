"""
------------------------------------------------------------------------
Lab 5, Task 12
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-10-15
------------------------------------------------------------------------
"""
num_rows = int(input("Enter a number: "))

for row in range(0, num_rows - 1):
#    print(">> Row {}".format(row))
    print("#", end='')
    for col in range(0, (row - 1)):
        print(" ",end='')
    if row >= 1:
        print("#")
    else:
        print()

for i in range(0, num_rows):
    print("#",end='')