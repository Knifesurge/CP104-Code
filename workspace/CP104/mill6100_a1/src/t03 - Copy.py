"""
------------------------------------------------------------------------
Assignment 1, Task 3
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-14
------------------------------------------------------------------------
"""
cost_of_pizza = float(input("Cost of 1 pizza: $"))
num_pizzas = int(input("Number of pizzas: "))
total = num_pizzas * cost_of_pizza

print("Total cost of {} pizzas: ${:.2f}".format(num_pizzas, total))