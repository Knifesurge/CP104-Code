"""
------------------------------------------------------------------------
Assignment 3, Task 3
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-21
------------------------------------------------------------------------
"""
player1_choice = input("Enter Player 1 choice (R, P, or S): ")
player2_choice = input("Enter Player 2 choice (R, P, or S): ")

if player1_choice == "R":
    if player2_choice == "R":
        print("A Tie!")
    elif player2_choice == "P":
        print("Paper beats Rock! Player 2 wins!")
    else:
        print("Rock beats Scissors! Player 1 wins!")
elif player1_choice == "P":
    if player2_choice == "R":
        print("Paper beats Rock! Player 1 wins!")
    elif player2_choice == "P":
        print("A Tie!")
    else:
        print("Rock beats Scissors! Player 2 wins!")
elif player1_choice == "S":
    if player2_choice == "R":
        print("Rock beats Scissors! Player 2 wins!")
    elif player2_choice == "P":
        print("Scissors beats Paper! Player 1 wins!")
    else:
        print("A Tie!")
