"""
------------------------------------------------------------------------
Lab 3, Task 4
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-09-18
------------------------------------------------------------------------
"""
age = int(input("Enter your age: "))
resting_heart_rate = int(input("Enter your resting heart rate: "))
exercise_heart_rate = int(input("Enter your heart rate during exercise: "))

max_heart_rate = 220 - age
thr = int(((max_heart_rate - resting_heart_rate) * (60/100)) + resting_heart_rate)

print("Your training heart rate is {}".format(thr))

if thr < exercise_heart_rate:
    print("Keep up your exercise program")
