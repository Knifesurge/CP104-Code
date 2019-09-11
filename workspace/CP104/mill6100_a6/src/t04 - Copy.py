"""
------------------------------------------------------------------------
Assignment 6, Task 4
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-05
------------------------------------------------------------------------
"""
from functions import fraction_product

num1 = int(input("Enter numerator of fraction 1: "))
den1 = int(input("Enter denominator of fraction 1: "))
num2 = int(input("Enter numerator of fraction 2: "))
den2 = int(input("Enter denominator of fraction 2: "))

num, den, product = fraction_product(num1, den1, num2, den2)

print("Product: {}/{}".format(num, den))
print("Fraction: {:.2f}".format(product))