"""
------------------------------------------------------------------------
Lab 9, Task 10
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-19
------------------------------------------------------------------------
"""
from functions import count_frequency_word

file_handle = open('words.txt', 'r')
print("file 'words.txt' open for reading")
word = input("Word to count: ")
count = count_frequency_word(file_handle, word)
file_handle.close()

print("'{}' appears {} time(s).".format(word, count))