"""
------------------------------------------------------------------------
Lab 5, Task 7
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-10-15
------------------------------------------------------------------------
"""
num_starting_bottles = int(input("Enter number of bottles: "))

for num_bottles in range(num_starting_bottles, 1, -1):
    next_bottles = num_bottles - 1
    print("{} bottles of beer on the wall, {} bottles of beer.".format(num_bottles, num_bottles))
    if next_bottles == 1:
        print("Take one down, pass it around, {} bottle of beer on the wall.".format(next_bottles))
    else:
        print("Take one down, pass it around, {} bottles of beer on the wall.".format(next_bottles))
    
print("1 bottle of beer on the wall, 1 bottle of beer.")
print("Take one down, pass it around, no more bottles of beer on the wall!")