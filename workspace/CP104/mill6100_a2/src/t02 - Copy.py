"""
------------------------------------------------------------------------
Assignment 2, Task 2
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-17
------------------------------------------------------------------------
"""
student_discount = 20
movie_cost = float(input("Cost of movie: $"))
student_cost = movie_cost - (movie_cost * (student_discount / 100))
print("The cost of the movie for a student is ${:.2f}".format(student_cost))
