"""
------------------------------------------------------------------------
Assignment 2, Task 4
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-17
------------------------------------------------------------------------
"""
amt_borrowed = float(input("Amount borrowed: $"))
interest_rate = (float(input("Interest rate: "))) / 100
length_of_loan = int(input("Length of loan (months): "))

monthly_payment = ((interest_rate / 12) * amt_borrowed) / (1 - (1 + (interest_rate / 12))**(-length_of_loan))
print("The monthly payment is ${:,.2f}".format(monthly_payment))