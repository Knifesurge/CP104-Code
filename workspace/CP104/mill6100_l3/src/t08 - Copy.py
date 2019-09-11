"""
------------------------------------------------------------------------
Lab 3, Task 8
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-20
------------------------------------------------------------------------
"""
MIN_HOURS_FOR_OVERTIME = 40 # Minimum amount of hours worked to qualify for overtime

hourly_pay_rate = float(input("Hourly pay rate: $"))
hours_worked = int(input("Hours worked: "))

total_pay = hourly_pay_rate * hours_worked

if hours_worked > MIN_HOURS_FOR_OVERTIME:
    overtime_hours = hours_worked - MIN_HOURS_FOR_OVERTIME
    total_pay += overtime_hours * (hourly_pay_rate * 150/100)

print("This week's pay is: ${:,.2f}".format(total_pay))