"""
------------------------------------------------------------------------
Assignment 6, Task 2
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-03
------------------------------------------------------------------------
"""
from functions import payment

principal = float(input("Amount borrowed: $"))
interest = float(input("Interest rate: "))
months = int(input("Length of loan (months): "))

total = payment(principal, interest, months)

print("The monthly payment is ${:,.2f}".format(total))
