"""
------------------------------------------------------------------------
Lab 3, Task 5
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-19
------------------------------------------------------------------------
"""
TEACHER_DISCOUNT = 10/100   # 10%
SALES_TAX = 5/100   # 5%

subtotal = float(input(("Total purchase: $")))
is_teacher = input("Is the customer a teacher (Y/N)? ")

if is_teacher == "Y":
    total_teacher_discount = subtotal * TEACHER_DISCOUNT
    print("Teacher's discount (10%): ${:>2,.2f}".format(total_teacher_discount))
    discount_total = subtotal - total_teacher_discount
    print("Discounted total:         ${:>2,.2f}".format(discount_total))
    total_with_tax = discount_total * SALES_TAX
    print("Sales tax:                ${:>2,.2f}".format(total_with_tax))
    total = discount_total + total_with_tax
    print("Total:                    ${:>2,.2f}".format(total))
else:
    total_with_tax = subtotal * SALES_TAX
    print("Sales tax:                ${:>2,.2f}".format(total_with_tax))
    total = subtotal + total_with_tax
    print("Total:                    ${:>2,.2f}".format(total))