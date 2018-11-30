"""
------------------------------------------------------------------------
Assignment 3, Task 5
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-21
------------------------------------------------------------------------
"""
"""
    25% discount b/w 1800 & 0000
    50% discount b/w 0000 & 0800
    10% discount for 30 mins or longer
    
    time of call placed applies BEFORE length discount
"""
BASE_CALL_COST = 8/100  # $0.08 => 8 cents / min

call_length = int(input("Length of call (minutes): "))
hour_of_call = int(input("Hour of call (24 hour format): "))

cost_of_call = BASE_CALL_COST * call_length

if hour_of_call >= 18 or hour_of_call < 0:
    cost_of_call -= cost_of_call * (1/4)    # Apply 25% discount
elif hour_of_call >= 0 or hour_of_call < 8:
    cost_of_call -= cost_of_call * (1/2)    # Apply 50% discount

if call_length >= 30:
    cost_of_call -= cost_of_call * (1/10)   # Apply 10% discount
    
print("Total price of call: ${:,.2f}".format(cost_of_call))