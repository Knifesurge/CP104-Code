"""
------------------------------------------------------------------------
Assignment 4, Task 3
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-10-03
------------------------------------------------------------------------
"""
candy_limit = int(input("Mom's limit on the number of candies: "))

num_candies = int(input("Candies from the first household: "))

while num_candies < candy_limit:
    num_candies += int(input("Candies from the next household: "))
    
print("\nYou have acquired {:,} candies in total".format(num_candies))

if num_candies > candy_limit:
    over_limit = num_candies % candy_limit
    print("You have {} candies over Mom's limit.".format(over_limit))