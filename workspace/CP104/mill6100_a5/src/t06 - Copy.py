"""
------------------------------------------------------------------------
Assignment 5, Task 6
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-02
------------------------------------------------------------------------
"""
start = int(input("Starting value for table: "))
end = int(input("Ending value for table: "))
# Print the first number
print("{:>11d}".format(start), end='')

# Print the remaining numbers
for num in range(start + 1, end + 1):
    print("{:>5d} ".format(num), end='')

print()
print("\t",end='')

# Print the hyphens to separate table
for num in range(15):
    print("{:->3s}".format(""), end='')
    
print()

# Print the left-side of the table, as well as fill in the table
for first in range(start, end + 1):
    print("{:>5d} | ".format(first), end='')
    for second in range(start, end + 1):
        product = first * second
        print("{:>5d}".format(product), end='')
    print()