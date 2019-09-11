"""
------------------------------------------------------------------------
Assignment 5, Task 5
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-01
------------------------------------------------------------------------
"""
num_values = int(input("Number of values: "))

negative_values = 0
zero_values = 0
positive_values = 0
even_values = 0
odd_values = 0
min_value = 0
max_value = 0
average = 0
total = 0

user_value = int(input("First value: "))

if user_value > 0:
    positive_values += 1
elif user_value < 0:
    negative_values += 1
else:
    zero_values += 1
      
if user_value % 2 == 0:
    even_values += 1
else:
    odd_values += 1
  
if user_value > max_value:
    max_value = user_value
elif user_value < min_value:
    min_value = user_value
        
total += user_value

for num in range(num_values - 1):
    if user_value > 0:
        positive_values += 1
    elif user_value < 0:
        negative_values += 1
    else:
        zero_values += 1
        
    if user_value % 2 == 0:
        even_values += 1
    else:
        odd_values += 1
    
    if user_value > max_value:
        max_value = user_value
    elif user_value < min_value:
        min_value = user_value
        
    total += user_value
    user_value = int(input("Next value: "))
    
average = total / num_values
print("Negative values:     {}".format(negative_values))
print("Zero values:         {}".format(zero_values))
print("Positive values:     {}".format(positive_values))
print("Even values:         {}".format(even_values))
print("Odd values:          {}".format(odd_values))
print("Total:               {}".format(total))
print("Minimum:             {}".format(min_value))
print("Maximum:             {}".format(max_value))
print("Average:             {}".format(average))