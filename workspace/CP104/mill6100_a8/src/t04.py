"""
------------------------------------------------------------------------
Assignment 8, Task 4
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-20
------------------------------------------------------------------------
"""
from functions import set_trials

subjects = [1, 2, 3, 4, 5, 6, 7]
# subjects = ["Terry", "Jane", "Matthew", "James", "Alice", "Mary"]
print("Subjects: {}".format(subjects))

drugs, placebos = set_trials(subjects)
print("Drug trial: {}".format(drugs))
print("Placebo trial: {}".format(placebos))