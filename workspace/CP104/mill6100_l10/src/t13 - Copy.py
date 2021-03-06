"""
------------------------------------------------------------------------
Lab 10, Task 13
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-26
------------------------------------------------------------------------
"""
from functions import find_word_diagonal, words_to_matrix, print_matrix_char

strings = ["cdb", "aoa", "tgt"]
print("String: {}".format(strings))

matrix = words_to_matrix(strings)

print_matrix_char(matrix)

word = input("\nThe word to search for: ")

found = find_word_diagonal(matrix, word)

if found:
    print("The word is found on the diagonal")
else:
    print("The word is not found on the diagonal")