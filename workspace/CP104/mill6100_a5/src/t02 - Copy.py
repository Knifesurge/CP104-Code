"""
------------------------------------------------------------------------
Assignment 5, Task 2
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-01
------------------------------------------------------------------------
"""
diamond_width = int(input("Width of diamond: "))
character = input("Printing character: ")

for i in range(1, diamond_width + 1):
    for j in range(i):
        print(character,end='')
    print()
    
for i in range(diamond_width, 1, -1):
    for j in range(i, 0, -1):
        print(character, end='')
    print()