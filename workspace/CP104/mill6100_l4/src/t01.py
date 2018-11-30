"""
------------------------------------------------------------------------
Lab 4, Task 1
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-27
------------------------------------------------------------------------
"""
from random import randint
number = randint(0, 100)

guess = int(input("Guess: "))

while guess != number:
    if guess > number:
        print("Too high, try again.")
    elif guess < number:
        print("Too low, try again")
    
    guess = int(input("Guess: "))
    
print("Congratulations - good guess!")