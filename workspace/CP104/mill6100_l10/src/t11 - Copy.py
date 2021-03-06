"""
------------------------------------------------------------------------
Lab 10, Task 11
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-26
------------------------------------------------------------------------
"""
from functions import find_word_horizontal, words_to_matrix, print_matrix_char

strings = ["cat", "dog", "bat"]
print("Strings: {}".format(strings))
print("Matrix of characters: ")
matrix = words_to_matrix(strings)

print_matrix_char(matrix)

word = input("\nThe word to search for: ")

rows = find_word_horizontal(matrix, word)

print("\nThe word is found in rows [{}]".format(rows))