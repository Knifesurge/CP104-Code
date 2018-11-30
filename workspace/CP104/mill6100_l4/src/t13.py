"""
------------------------------------------------------------------------
Lab 4, Task 13
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-28
------------------------------------------------------------------------
"""
number = int(input("Enter an integer: "))
number_temp = number
total = 1   # Anything multiplied by 1 is itself, so 1 is a good initial value

print("{}! = ".format(number), end='')

while number_temp > 0:
    total *= number_temp
    print("{} * ".format(number_temp), end = '')
    number_temp -= 1

print("= {}".format(total))