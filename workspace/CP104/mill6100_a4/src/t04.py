"""
------------------------------------------------------------------------
Assignment 4, Task 4
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-10-03
------------------------------------------------------------------------
"""
MINIMUM_BUDGET_PERCENTAGE = 90 / 100 # % of budget that needs to be reached

party_budget = float(input("Party budget: $"))
minimum_budget_spending = party_budget * MINIMUM_BUDGET_PERCENTAGE
item_cost = 0
total_cost = 0
another_item = ""
remaining_budget = party_budget

while another_item != "N":
    item_cost = float(input("Cost of item: $"))
    total_cost += item_cost
    another_item = input("Buy another item (Y/N): ")
    remaining_budget -= item_cost
    if another_item == "N" and total_cost < minimum_budget_spending:
        print("Have not yet spent the minimum amount: ${:,.2f}".format(minimum_budget_spending))
        another_item = ""
    elif item_cost > (party_budget - total_cost):
        print("Item costs too much: ${:,.2f} remaining in budget".format(remaining_budget))
        
print("Total spent on items: ${:,.2f}".format(total_cost))