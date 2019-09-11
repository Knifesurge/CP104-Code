"""
------------------------------------------------------------------------
Assignment 3, Task 4
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-21
------------------------------------------------------------------------
"""
""" Assume that the user enters a valid colour name """
colour1 = input("Enter first colour: ")
colour2 = input("Enter second colour: ")
secondary_colour = ""

if colour1 == "red":
    if colour2 == "blue":
        secondary_colour = "purple"
    elif colour2 == "yellow":
        secondary_colour = "orange"
    else:   # colour2 == 'red'
        print("No secondary colour")
        exit()
elif colour1 == "blue":
    if colour2 == "red":
        secondary_colour = "purple"
    elif colour2 == "yellow":
        secondary_colour = "green"
    else:   # colour2 == 'blue'
        print("No secondary colour")
        exit()
else:   # colour1 == 'yellow'
    if colour2 == "red":
        secondary_colour = "orange"
    elif colour2 == "blue":
        secondary_colour = "green"
    else:   # colour2 == 'yellow'
        print("No secondary color")
        exit()

print("Secondary colour is {}".format(secondary_colour))