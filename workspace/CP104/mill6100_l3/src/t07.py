"""
------------------------------------------------------------------------
Lab 3, Task 7
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-19
------------------------------------------------------------------------
"""
GREAT_AVERAGE = 90  # Average must be higher than this to receive congratulations

test1 = int(input("Grade for test 1: "))
test2 = int(input("Grade for test 2: "))
test3 = int(input("Grade for test 3: "))

average = (test1 + test2 + test3) // 3  # Use integer division

print("The average: {}".format(average))

if average > GREAT_AVERAGE:
    print("Congratulations, great average!")
