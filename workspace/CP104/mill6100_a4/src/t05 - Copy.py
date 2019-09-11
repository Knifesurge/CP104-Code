"""
------------------------------------------------------------------------
Assignment 4, Task 5
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-10-04
------------------------------------------------------------------------
"""
# Program Constants
SENIOR_AGE = 65
SENIOR_PRICE = 4.0
ADULT_AGE = 18
ADULT_PRICE = 5.0
INFANT_AGE = 3
INFANT_PRICE = 0
STUDENT_AGE_LO = 10
STUDENT_AGE_HI = 15
STUDENT_PRICE = 1.0
KID_PRICE = 2.0

total_price = 0

another_purchase = input("Purchase a ticket (Y/N)? ")

while another_purchase != "N":
    age = int(input("How old are you? "))
    if age >= SENIOR_AGE:
        total_price += SENIOR_PRICE
        print("That ticket costs ${:,.2f}".format(SENIOR_PRICE))
    elif age >= ADULT_AGE:
        total_price += ADULT_PRICE
        print("That ticket costs ${:,.2f}".format(ADULT_PRICE))
    elif age >= STUDENT_AGE_LO and age <= STUDENT_AGE_HI:
        student = input("Are you a student at this school? (Y/N) ")
        if student == "Y":
            total_price += STUDENT_PRICE
            print("That ticket costs ${:,.2f}".format(STUDENT_PRICE))
        else:
            total_price += KID_PRICE
            print("That ticket costs ${:,.2f}".format(KID_PRICE))
    elif age <= 3:
        print("You get in for free.")
    else:   # Children b/w age of 4 and 9
        total_price += KID_PRICE
        print("That ticket costs ${:,.2f}".format(KID_PRICE))
    another_purchase = input("Purchase another ticket (Y/N)? ")
        
print("Total tickets price: ${:,.2f}".format(total_price))