"""
------------------------------------------------------------------------
Assignment 4, Task 6
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-10-14
------------------------------------------------------------------------
"""
from random import randint

again = ""
num_correct = 0
count = 0

while again != "N":
    count += 1
    number1 = randint(0, 1000)
    number2 = randint(0, 1000)

    print("{:>5d}".format(number1))
    print("+{:>4d}".format(number2))
    answer = number1 + number2
    user_answer = int(input("= "))
    
    if user_answer == answer:
        print("Congratulations!")
        num_correct += 1
    else:
        print("Sorry, the correct answer is {}".format(answer))
    
    again = input("\nContinue (Y/N): ")
    
print("\nYour final score is {}/{}".format(num_correct, count))