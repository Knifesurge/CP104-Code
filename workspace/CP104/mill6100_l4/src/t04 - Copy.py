"""
------------------------------------------------------------------------
Lab 4, Task 4
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-27
------------------------------------------------------------------------
"""
monthly_budget = float(input("Monthly budget: $"))
total_expenses = 0
expense = float(input("Enter an expense (0 to quit): $"))

while expense != 0:
    total_expenses += expense
    expense = float(input("Enter another expense (0 to quit): $"))
    
end_result = abs(monthly_budget - total_expenses)

if end_result < monthly_budget: # Surplus
    print("Surplus: ${:,.2f}".format(end_result))
elif end_result > monthly_budget:   # Deficit
    print("Deficit: ${:,.2f}".format(end_result))
else:   # Balanced
    print("Balanced")