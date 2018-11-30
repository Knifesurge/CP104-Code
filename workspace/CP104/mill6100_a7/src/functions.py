"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-13
------------------------------------------------------------------------
"""
def my_isdigit(s):
    """
    -------------------------------------------------------
    Determines if all the characters is s are digits. An empty string
    has no digits.
    NOTE: must execute as the equivalent of the Python method s.isdigit()
    Use: digits = my_isdigit(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        digits - True if all of s is digits, False otherwise (boolean)
    -------------------------------------------------------
    """
    DIGITS = "0123456789"
    all_digits = False  # Defaults to False, empty string handled
    for char in s:
        if char in DIGITS:
            all_digits = True
        else:
            all_digits = False
            break
    
    return all_digits

def my_isalpha(s):
    """
    -------------------------------------------------------
    Determines if all the characters is s are alphabetic characters.
    An empty string has no letters.
    NOTE: must execute as the equivalent of the Python method s.isalpha()
    Use: alpha = my_isalpha(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        alpha - True if all of s is letters of the alphabet,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    all_letters = False
    for char in s:
        if char in LETTERS:
            all_letters = True
        else:
            all_letters = False
            break
            
    return all_letters

def my_find(s, r):
    """
    -------------------------------------------------------
    Returns the index of the string r in the string s.
    NOTE: must execute as the equivalent of the Python method s.find(r)
    Use: i = my_find(s, r)
    -------------------------------------------------------
    Parameters:
        s - a string to search (str)
        r - a string to search for (str)
    Returns:
        i - the index of the start of r in s, -1 if r is not in s (int)
    -------------------------------------------------------
    """
    """ Uses the Native Algorithm for Pattern Searching """
    M = len(r)
    N = len(s)
    index = -1
    
    i = 0
    while i <= (N - M):
        # Check pattern match for current index
        for j in range(M):
            if s[i + j] != r[j]:
                break
            j += 1
        
        if j == M:
            index = i
            i += M
        elif j == 0:
            i += 1
        else:
            i += j
            
    return index

def common_ending(s1, s2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: common = common_ending(s1, s2)
    -------------------------------------------------------
    Parameters:
        s1 - first string for ending comparison (str)
        s2 - second string for ending comparison (str)
    Returns:
        common - the longest common ending of s1 and s2 (str)
    -------------------------------------------------------
    """
    index = -1
    s1_reversed = s1[::-1]
    s2_reversed = s2[::-1]
    shortest = None
    if len(s1) > len(s2):
        shortest = s2_reversed
    else:
        shortest = s1_reversed
    for i in range(len(shortest)):
        if s1_reversed[i] == s2_reversed[i]:
            index = i + 1
        else:
            break
    new_index = len(s1) - index
    common = s1[new_index:] 
    return common
    
def is_valid_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: valid = is_valid_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """
    valid = False
    groups = isbn.split("-")
    last_digit = True
    
    if len(isbn) == 17:
        if groups[0] in ["978", "979"]:
            if isbn.count("-") == 4:
                if groups[-1] in "0123456789":
                    for group in groups:
                        if not group:   # Empty
                            valid = False
                            break
                        else:
                            for digit in group:
                                if digit.isdigit() and last_digit:
                                    valid = True
                                else:
                                    valid = False
                                    last_digit = False
                                    break
                                
    return valid

def number_convert(number):
    """
    -------------------------------------------------------
    Converts a phone number character string to a string of digits.
    A telephone keypad has the following digit/letter combinations:
        2 : ABC
        3 : DEF
        4 : GHI
        5 : JKL
        6 : MNO
        7 : PRS
        8 : TUV
        9 : WXY
    ('Q' and 'Z' are not represented.) Q, Z, and non-letters are
    left unchanged.
    Use: digits = number_convert(number)
    -------------------------------------------------------
    Parameters:
        number - a phone number string (str)
    Returns:
        digits - the numeric version of number based upon a
            telephone keypad (str)
    -------------------------------------------------------
    """
    """    groups = number.split("-")
    digits = groups
    for i in range(len(groups)):
        for j in groups[i]:
            if j in "ABC":
                for letter in j:
                    print("B: {}".format(letter))
                    letter.remove()
                    letter.insert(0, "2")
                    print("A: {}".format(letter))
                    digits.append(groups[i][j.index(letter)])
    """
    LETTERS = "ABCDEFGHIJKLMNOPRSTUVWXY"
    NUMS = "222333444555666777888999"
    trans = number.maketrans(LETTERS, NUMS)
    return number.translate(trans)

def pluralize(s):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if s ends with 's', 'sh', or 'ch', add 'es'
        - if s ends with 'y' but not 'ay' or 'oy', add 'ies'
        - otherwise add 's'
    Use: plural = pluralize(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        plural - a plural version of s (str)
    -------------------------------------------------------
    """
    plural = ""
    if s.endswith("s") or s.endswith("sh") or s.endswith("ch"):
        plural = s + "es"
    elif s.endswith("y") and not (s.endswith("ay") or s.endswith("oy")):
        plural = s[:-1] + "ies"
    else:
        plural = s + "s"
    
    return plural