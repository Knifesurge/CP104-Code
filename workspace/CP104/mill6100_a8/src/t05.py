"""
------------------------------------------------------------------------
Assignment 8, Task 5
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-22
------------------------------------------------------------------------
"""
from functions import license_test

# correct_answers = ["A", "B", "B", "C", "D", "A", "C", "B"]
# student_answers = ["A", "B", "D", "C", "D", "A", "C", "C"]
correct_answers = [1, 2, 3, 2, 1, 1, 2, 3, 1, 1, 2, 3]
student_answers = [1, 2, 3, 2, 1, 1, 2, 3, 1, 1, 2, 3]

correct, incorrect, list_incorrect = license_test(correct_answers, student_answers)
print("Correct Answers: {}".format(correct_answers))
print("Student Answers: {}".format(student_answers))
print("Correct Answers Count: {}".format(correct))
print("Incorrect Answers Count: {}".format(incorrect))
print("Indexes of Incorrect Answers: {}".format(list_incorrect))