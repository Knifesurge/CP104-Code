"""
------------------------------------------------------------------------
Lab 4, Task 5
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-28
------------------------------------------------------------------------
"""
budget = float(input("Enter budget: $"))
daily_expense = 0
total_expenses = 0

for day in range(1,8):
    daily_expense = float(input("Expenses for day {}: $".format(day)))
    total_expenses += daily_expense
    
print("\nExpenses: ${:,.2f}".format(total_expenses))
balance = budget - total_expenses
print("Balance: ${:,.2f}".format(balance))
