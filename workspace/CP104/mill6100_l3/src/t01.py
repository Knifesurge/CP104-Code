"""
------------------------------------------------------------------------
Lab 3, Task 1
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-18
------------------------------------------------------------------------
"""
MEMBERSHIP_DISCOUNT = 5 / 100   # Basic membership discount

membership_cost = float(input("Gym membership cost: $"))
num_friends = int(input("Number of friends signed up: "))

if num_friends == 1:
    total_discount = MEMBERSHIP_DISCOUNT
elif num_friends == 2:
    total_discount = 2 * MEMBERSHIP_DISCOUNT
elif num_friends >= 3:
    total_discount = 3 * MEMBERSHIP_DISCOUNT
else:
    total_discount = 0
    
total_cost = membership_cost - (membership_cost * total_discount)

print("Your membership cost is ${:,.2f}".format(total_cost))