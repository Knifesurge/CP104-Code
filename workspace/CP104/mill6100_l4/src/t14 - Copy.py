"""
------------------------------------------------------------------------
Lab 4, Task 14
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-29
------------------------------------------------------------------------
"""
""" Original can be found at https://www.programiz.com/python-programming/examples/prime-number 
    This is a modified version of above link.
"""
number = int(input("Enter an integer: "))

if number > 1:  # Any primes are greater than 1
    for i in range(2, number):  # Check for any factors
        if (number % i) == 0:
            print("It is not a prime number.")
            break
        else:
            print("It is a prime number.")
            break
else:
    print("It is not a prime number.")