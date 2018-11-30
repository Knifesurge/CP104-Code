"""
------------------------------------------------------------------------
Lab 4, Task 2
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-27
------------------------------------------------------------------------
"""
day_num = 0
another_day = "Y"
grand_total = 0
breakfast_total = 0
lunch_total = 0
supper_total = 0

while another_day != "N":
    day_num += 1
    print("For Day {}".format(day_num), end='\n\n')
    breakfast_cost = float(input("How much was breakfast? $"))
    lunch_cost = float(input("How much was lunch? $"))
    supper_cost = float(input("How much was supper? $"))
    total_for_day = breakfast_cost + lunch_cost + supper_cost
    print("Your total for the day was ${:,.2f}".format(total_for_day), end="\n\n")
    breakfast_total += breakfast_cost
    lunch_total += lunch_cost
    supper_total += supper_cost
    grand_total += total_for_day
    another_day = input("Were you away another day (Y/N)? ")
    print()

print("Total:")
print("Breakfast:  ${:,.2f}".format(breakfast_total))
print("Lunch:      ${:,.2f}".format(lunch_total))
print("Supper:     ${:,.2f}".format(supper_total), end='\n\n')

print("Grand total: ${:,.2f}".format(grand_total))