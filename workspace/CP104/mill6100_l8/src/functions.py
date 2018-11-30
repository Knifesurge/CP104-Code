"""
------------------------------------------------------------------------
Holds functions for modules
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-10
------------------------------------------------------------------------
"""
from random import randint
def get_weekday_name(d):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given its number.
    Use: name = get_weekday_name(d)
    -------------------------------------------------------
    Parameters:
        d - day of week number (1 <= int <= 7)
    Returns:
        name - matching day of the week, 1 = "Sunday", 7 = "Saturday" (str)
    -------------------------------------------------------
    """
    DAYS_OF_WEEK = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return DAYS_OF_WEEK[d - 1]

def get_month_name(m):
    """
    -------------------------------------------------------
    Returns the name of a month given its number.
    Use: name = get_month_name(m)
    -------------------------------------------------------
    Parameters:
        m - month number (int 1 <= m <= 12)
    Returns:
        name - matching month, 1 = "January", 12 = "December" (str)
    -------------------------------------------------------
    """
    NAMES_OF_MONTHS = ["January", "February", "March", "April", "May", "June", "July", 
                       "August", "September", "October", "November", "December"]
    return NAMES_OF_MONTHS[m - 1]

def get_digit_name(n):
    """
    -------------------------------------------------------
    Returns the name of a digit given its number.
    Use: name = get_digit_name(n)
    -------------------------------------------------------
    Parameters:
        n - digit number (int 0 <= n <= 9)
    Returns:
        name - matching digit, 0 = "zero", 9 = "nine" (str)
    -------------------------------------------------------
    """
    NAMES_OF_DIGITS = ["zero", "one", "two", "three", "four", "five",
                       "six", "seven", "eight", "nine"]
    return NAMES_OF_DIGITS[n]

def generate_integer_list(n, low, high):
    """
    -------------------------------------------------------
    Generates a list of random integers.
    Requires import: from random import randint
    Use: values = generate_integer_list(n, low, high)
    -------------------------------------------------------
    Preconditions:
        n - number of values to generate (int, > 0)
        low - low value range (int)
        high - high value range (int, > low)
    Postconditions:
        values - a list of random integers (list of int)
    -------------------------------------------------------
    """
    integer_list = []
    for i in range(n):
        integer_list.append(randint(low, high))
    return integer_list

def get_lotto_numbers(n, low, high):
    """
    -------------------------------------------------------
    Generates a sorted list of unique lottery numbers.
    Requires import: from random import randint
    Use: numbers = get_lotto_numbers(n, low, high)
    -------------------------------------------------------
    Parameters:
        n - number of lottery numbers to generate (int > 0)
        low - low value of the lottery number range (int >= 0)
        high - high value of the lottery number range (int > low)
    Returns:
        numbers - a list of unique random lottery numbers (list of int)
    -------------------------------------------------------
    """
    numbers = []
    for i in range(n):
        number = randint(low, high)
        if number not in numbers:
            numbers.append(number)
    return numbers

def list_stats(values):
    """
    -------------------------------------------------------
    Returns statistics about values in a list.
    values has at least one element.
    Use: smallest, largest, total, average = list_stats(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of float)
    Returns:
        smallest - the smallest number in values (float)
        largest - the largest number in values (float)
        total - total of numbers in list (float)
        average - the average numbers in values (float)
    -------------------------------------------------------
    """
    smallest = values[0]    # Defaults to first value in list
    largest = values[0]
    total = 0
    
    for i in range(len(values)):
        current_value = values[i]
        if current_value < smallest:
            smallest = current_value
        if current_value > largest:
            largest = current_value
        total += current_value
    
    count = len(values)
    average = total / count
    return smallest, largest, total, average

def list_categorize(values):
    """
    -------------------------------------------------------
    Returns data about the categories of values in a list.
    Use: negatives, positives, zeroes, evens, odds = list_categorize(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of int)
    Returns:
        negatives - the number of negative values (int)
        positives - the number of positive values (int)
        zeroes - the number of zeroes (int)
        evens - the number of even values (int)
        odds - the number of odd values (int)
    -------------------------------------------------------
    """
    negatives = 0
    positives = 0
    zeroes = 0
    evens = 0
    odds = 0
    for i in range(len(values)):
        current_value = values[i]
        if current_value < 0:
            negatives += 1
        elif current_value > 0:
            positives += 1
        else:   # Equals 0
            zeroes += 1
            
        if current_value % 2 == 0:
            evens += 1
        else:
            odds += 1
            
    return negatives, positives, zeroes, evens, odds

def linear_search(a, v):
    """
    -------------------------------------------------------
    Searches through a for the value v and returns its index.
    User: index = linear_search(a, v)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of ?).
        v - can be compared to values in a (?).
    Returns:
        index - the index of the location of v in a, -1 if not found (int).
    -------------------------------------------------------
    """
    index = -1  # Defaults to not being found
    for i in range(len(a)):
        if v == a[i]:
            index = i
    return index

def many_search(a, v):
    """
    -------------------------------------------------------
    Searches through a for the value v and returns a list of
    all indexes of its occurrence.
    User: indexes = many_search(a, v)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of ?).
        v - can be compared to values in a (?).
    Returns:
        indexes - a list of indexes of the location of v in a,
            [] if not found (list of int).
    -------------------------------------------------------
    """
    indexes = []
    for i in range(len(a)):
        if v == a[i]:
            indexes.append(i)
    return indexes

def min_search(a):
    """
    -------------------------------------------------------
    Searches through a for the minimum value(s) and returns a
    list of the indexes of those values. (Assumes a has at least
    one element.)
    User: indexes = min_search(a, v)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of ?).
    Returns:
        indexes - a list of indexes of the minimum values in 
            a (list of int).
    -------------------------------------------------------
    """
    indexes = []
    min_value = a[0]
    
    # Find the minimum value in the list
    for i in range(len(a)):
        if a[i] < min_value:
            min_value = a[i]
            indexes.append(i)            
    return indexes

def dot_product(source1, source2):
    """
    -------------------------------------------------------
    Calculates a dot product of two lists. Lists must be the
    same length.
    Use: target = dot_product(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - list of numbers (list of float)
        source2 - list of numbers (list of float)
    Returns:
        target - source1 � source2 [source1 dot product source2] (list of float)
    -------------------------------------------------------
    """
    target = []
    product = 0
    
    for i in range(len(source1)):
        val1 = source1[i]
        val2 = source2[i]
        target.append(val1 * val2)
        product += target[i]
               
    return product

def list_sums(source1, source2):
    """
    -------------------------------------------------------
    Calculates sums of elements of two lists. Lists must be the
    same length.
    Use: target = list_sum(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - list of numbers (list of float)
        source2 - list of numbers (list of float)
    Returns:
        target - sums of elements of source1 and source2 (list of float)
    -------------------------------------------------------
    """
    target = []
    
    for i in range(len(source1)):
        val1 = source1[i]
        val2 = source2[i]
        target.append(val1 + val2)        
    return target

def union(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the union of the contents of source1 and source2.
    Every element that appears at least once in either source1 and source2
    must appear once and only once in target.
    Use: target = union(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of ?)
        source2 - a list (list of ?)
    Returns:
        target - the union of source1 and source2 (list of ?)
    -------------------------------------------------------
    """
    target = []
    
    for i in range(len(source1)):
        if source1[i] not in target:
            target.append(source1[i])
            
    for i in range(len(source2)):
        if source2[i] not in target:
            target.append(source2[i])
            
    return target

def intersection(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the intersection of the contents of source1 and source2.
    Only elements that appear in both source1 and source2
    appear once and only once in target.
    Use: target = intersection(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of ?)
        source2 - a list (list of ?)
    Returns:
        target - the intersection of source1 and source2 (list of ?)
    -------------------------------------------------------
    """
    target = []
    for i in range(len(source1)):
        val1 = source1[i]
        if val1 in source2 and val1 not in target:
            target.append(val1)
                    
    return target

def symmetric_difference(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the symmetric difference of the contents
    of source1 and source2.
    Only elements that appear in one of source1 and source2
    appear once and only once in target.
    Use: target = symmetric_difference(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of ?)
        source2 - a list (list of ?)
    Returns:
        target - the symmetric difference of source1 and source2 (list of ?)
    -------------------------------------------------------
    """
    target = []
    for i in range(len(source1)):
        val1 = source1[i]
        if val1 not in source2:
            if val1 not in target:
                target.append(val1)
                
    for i in range(len(source2)):
        val = source2[i]
        if val not in source1:
            if val not in target:
                target.append(val)
    return target