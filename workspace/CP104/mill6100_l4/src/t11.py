"""
------------------------------------------------------------------------
Lab 4, Task 11
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-28
------------------------------------------------------------------------
"""
total_payroll = 0
average_payroll = 0
num_employees = 0

employee_id = int(input("Employee ID: "))

while employee_id != 0:
    hourly_rate = float(input("Hourly wage rate: "))
    hours_worked = int(input("Hours worked: "))
    overtime_hours = hours_worked % 40
    net_pay = ((hours_worked - overtime_hours) * hourly_rate) + (overtime_hours * (hourly_rate * 1.5))
    net_pay -= net_pay * (3.625 / 100)  # Tax deduction of 3.625%
    print("Net payment for employee {}: ${:,.2f}\n".format(employee_id, net_pay))
    total_payroll += net_pay
    num_employees += 1
    employee_id = int(input("Employee ID: "))
    
print("---------------------------")
print("Total payment:   ${:,.2f}".format(total_payroll))
average_payroll = total_payroll / num_employees
print("Average payment: ${:,.2f}".format(average_payroll))