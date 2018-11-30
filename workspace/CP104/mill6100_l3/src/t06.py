"""
------------------------------------------------------------------------
Lab 3, Task 6
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-19
------------------------------------------------------------------------
"""
MINIMUM_SALARY = 30000   # $30,000.00 or above
MINIMUM_YEARS_EMPLOYED = 2

annual_salary = float(input("Annual salary: "))
years_employed = int(input("Years employed: "))

if annual_salary < MINIMUM_SALARY:
    print("You must earn at least $30,000 per year to qualify for a loan")
elif years_employed < MINIMUM_YEARS_EMPLOYED:
    print("You must have been employed for at least 2 years to qualify for a loan")
else:
    print("You qualify for a loan!")
