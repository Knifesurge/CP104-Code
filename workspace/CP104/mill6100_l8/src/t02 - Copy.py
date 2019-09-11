"""
------------------------------------------------------------------------
Lab 8, Task 2
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-11
------------------------------------------------------------------------
"""
from functions import get_month_name

#for i in range(1, 12 + 1):
#    print(get_month_name(i))

month = int(input("Number of month: "))
month_name = get_month_name(month)
print("Month {} is: {}".format(month, month_name))