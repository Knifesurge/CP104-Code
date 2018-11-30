"""
------------------------------------------------------------------------
Assignment 2, Task 1
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-17
------------------------------------------------------------------------
"""
profit_percentage = 0.18    # Annual profit typically increases by 18%
projected_annual_sales = float(input("Enter projected annual sales: $"))

projected_profit = projected_annual_sales * profit_percentage
print("The projected profit on sales of ${:,.2f} is ${:,.2f}.".format(projected_annual_sales, projected_profit))
