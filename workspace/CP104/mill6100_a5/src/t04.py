"""
------------------------------------------------------------------------
Assignment 5, Task 4
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-01
------------------------------------------------------------------------
"""
num_years = int(input("Number of years of rainfall: "))

total_rainfall = 0
num_months = 0
average_rainfall = 0

print("Enter rainfall in cm")

for year in range(1, num_years + 1):
    print("Year {}".format(year))
    for month in range(1, 12 + 1):
        total_rainfall += float(input(("{:>5s} {:>2d}: ".format("Month", month))))
        num_months += 1
        
print("Number of months: {}".format(num_months))
print("Total rainfall: {:.2f} cm".format(total_rainfall))
average_rainfall = total_rainfall / num_months
print("Average rainfall per month: {:.2f} cm".format(average_rainfall))