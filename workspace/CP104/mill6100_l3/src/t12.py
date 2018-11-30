"""
------------------------------------------------------------------------
Lab 3, Task 12
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-20
------------------------------------------------------------------------
"""
number = int(input("Enter a number from 1 to 10: "))
roman_numeral = None

if number == 1:
    roman_numeral = "I"
elif number == 2:
    roman_numeral = "II"
elif number == 3:
    roman_numeral = "III"
elif number == 4:
    roman_numeral = "IV"
elif number == 5:
    roman_numeral = "V"
elif number == 6:
    roman_numeral = "VI"
elif number == 7:
    roman_numeral = "VII"
elif number == 8:
    roman_numeral = "VIII"
elif number == 9:
    roman_numeral = "IX"
elif number == 10:
    roman_numeral = "X"
else:
    print("None.")
    exit()  # To prevent following print statement from printing
    
print("The roman numeral equivalent of {} is {}".format(number, roman_numeral))