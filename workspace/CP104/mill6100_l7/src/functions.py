"""
------------------------------------------------------------------------
Module to hold all functions used in task modules
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-04
------------------------------------------------------------------------
"""
def is_hydroxide(chemical):
    """
    -------------------------------------------------------
    Determines if a chemical formula is a hydroxide.
    Use: hydroxide = is_hydroxide(chemical)
    -------------------------------------------------------
    Preconditions:
        chemical - a chemical formula (str)
    Postconditions:
        hydroxide - True if chemical is a hydroxide (ends in 'OH'),
            False otherwise (boolean)
    -------------------------------------------------------
    """
    return chemical.endswith("OH")

def url_categorize(url):
    """
    -------------------------------------------------------
    Returns whether a url represents a business, a non-profit, or another
    type of organization.
    Use: url_type = org_categorize(url)
    -------------------------------------------------------
    Parameters:
        url - the web address of the organization (str)
    Returns:
        url_type - the organization type (str)
            'business' if url ends with 'com'
            'non-profit' if url ends with 'org'
            'other' if url ends with something else
    ------------------------------------------------------
    """
    if url.endswith("com"):
        return "business"
    elif url.endswith("org"):
        return "non-profit"
    else:
        return "other"
    
def parse_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code. A product code has three parts:
        The first three letters describe the product category
        The next four digits are the product ID
        The remaining characters describe the product's qualifiers
    Use: pc, pi, pq = parse_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a valid product code (str)
    Returns:
        pc - the category part of product_code (str)
        pi - the id part of product_code (str)
        pq - the qualifier part of product_code (str)
    -------------------------------------------------------
    """
    pc = product_code[0:3]
    pi = product_code[3:7]
    pq = product_code[7:]
    return pc, pi, pq

def validate_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code and prints whether the various parts are valid.
    A product code has three parts: 
        The first three letters describe the product category and must 
        all be in upper case.
        The next four digits are the product ID.
        The remaining characters describe the product's qualifiers, 
        such as colour, size, etc. and always begins with an uppercase letter.
    Use: validate_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a product code (str)
    Returns:
        None
    -------------------------------------------------------
    """
    if len(product_code) < 8:
        print("Product code not long enough")
        return
    
    pc = product_code[0:3]
    if pc.isupper() and pc.isalpha():
        print("Category {} is valid.".format(pc))
    else:
        print("Category {} is not valid.".format(pc))
    
    pi = product_code[3:7]
    if pi.isdigit():
        print("ID {} is valid.".format(pi))
    else:
        print("ID {} is not valid.".format(pi))
        
    pq = product_code[7:]
    if pq[0].isupper():
        print("Qualifier {} is valid.".format(pq))
    else:
        print("Qualifier {} is not valid.".format(pq))
        
    return  # To clearly indicate the end of the function    
        
def password_strength(password):
    """
    -------------------------------------------------------
    Checks the strength of a given password. A password is
    strong if it contains at least eight characters, has a
    combination of upper-case and lower-case letters, and
    includes digits. Prints one or more of:
        not long enough - if password less than 8 characters
        no digits - if password has no digits
        no upper case - if password has no upper case letters
        no lower case - if password has no lower case letters
    Use: passwd_strength(pass)
    -------------------------------------------------------
    Parameters:
        password - the password to be checked (str)
    Returns:
        None
    ------------------------------------------------------
    """
    if len(password) < 8:
        print("Not long enough")
        
    if password.isalpha():
        print("No digits")
    
    if password.islower():
        print("No upper case")
        
    if password.isupper():
        print("No lower case")
    
    return  # To clearly indicate the end of the function
        
def is_palindrome(s):
    """
    -----------------------------------------------------------------
    Checks whether the given string is palindrome or not. A palindrome is
    a string the reads the same forwards as backwards.
    Use: palindrome = is_palindrome(s)
    -----------------------------------------------------------------
    Parameters:
        s - a string to be checked (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -----------------------------------------------------------------
    """
    return s == s[::-1] # Reverses the string

def vowel_count(s):
    """
    -------------------------------------------------------
    Counts the number of vowels in a string. Does not include 'y'.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - the number of vowels in s (int)
    -------------------------------------------------------
    """
    # Work on a lowercase version of the string so only have to check lowercase vowels
    s_lower = s.lower()
    
    num_a = s_lower.count("a")
    num_e = s_lower.count("e")
    num_i = s_lower.count("i")
    num_o = s_lower.count("o")
    num_u = s_lower.count("u")
    
    count = num_a + num_e + num_i + num_o + num_u
    return count

def digit_count(s):
    """
    -------------------------------------------------------
    Counts the number of digits in a string.
    Use: count = digit_count(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - the number of digits in s (int)
    -------------------------------------------------------
    """
    count = 0
    for digit in s:
        if digit.isdigit():
            count += 1
            
    return count

def count_special_chars(s):
    """
    -------------------------------------------------------
    Counts the number of special characters in s.
    The special characters are: "#", "@", "$", "%", "&", "!".
    Use: count = count_special_chars(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - number of special characters in s (int)
    ------------------------------------------------------
    """
    num_pound = s.count("#")
    num_at = s.count("@")
    num_dollar = s.count("$")
    num_percent = s.count("%")
    num_ampersand = s.count("&")
    num_exclamation = s.count("!")
    
    count = num_pound + num_at + num_dollar + num_percent + num_ampersand + num_exclamation
    return count

def text_analyze(txt):
    """
    -------------------------------------------------------
    Analyzes txt and returns the number of uppercase letters,
    lowercase letters, digits, and number of whitespaces in txt.
    Use: uppr, lowr, dgts, whtspc = text_analyze(txt)
    -------------------------------------------------------
    Parameters:
        txt - the text to be analyzed (str)
    Returns:
        uppr - number of uppercase letters in txt (int >= 0)
        lowr - number of lowercase letters in txt (int >= 0)
        dgts - number of digits in txt (int >= 0)
        whtspc - number of white spaces in the text (int >= 0)
    ------------------------------------------------------
    """
    uppr = 0
    lowr = 0
    dgts = 0
    whtspc = 0
    
    for char in txt:
        if char.isupper():
            uppr += 1
        elif char.islower():
            lowr += 1
        elif char.isdigit():
            dgts += 1
        elif char.isspace():
            whtspc += 1
    
    return uppr, lowr, dgts, whtspc

def dsmvwl(s):
    """
        -------------------------------------------------------
    Disemvowels a string. Returns a copy of s with all the vowels
    removed. Y is not treated as a vowel. Preserves case.
    Use: out = dsmvwl(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        out - s with its vowels removed (str)
    -------------------------------------------------------
    """
    new_str = s
    vowels = ("a", "A", "e", "E", "i", "I", "o", "O", "u", "U")
    for char in s:
        if char in vowels:
            new_str = new_str.replace(char, "")
    return new_str

def comma_period_replace(s):
    """
    -------------------------------------------------------
    Replaces all the commas with a period in s.
    Use: out = comma_period_replace(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        out - s with all commas replaced by a period (str)
    ------------------------------------------------------
    """
    new_str = s
    for char in s:
        if char in ',':
            new_str = new_str.replace(char, ".")
            
    return new_str

def total_digits(s):
    """
    -------------------------------------------------------
    Extracts and calculates the total of all digits in s.
    Use: total = total_digits(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        total - total of all the digits in s (int)
    ------------------------------------------------------
    """
    digits = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
    count = 0
    for char in s:
        if char in digits:
            count += 1
            
    return count

def str_distance(s1, s2):
    """
    -------------------------------------------------------
    Finds the distance between the s1 and s2. The distance between two
    strings of the same length is the number of positions in the strings
    at which their characters are different. If two strings are not the
    same length, the distance is unknown (-1). If the distance is zero,
    then two strings are equal.
    Use: d = str_distance(s1, s2)
    -------------------------------------------------------
    Parameters:
        s1 - first string (str)
        s2 - second string (str)
    Returns:
        d - the distance between s1 and s2 (int)
    ------------------------------------------------------
    """
    if len(s1) != len(s2):
        return -1
    
    if s1 == s2:
        return 0
    
    d = 0
    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            d +=1
        if s1[i] == s2[i]:
            return d
    return d

def calculate(expr):
    """
    -----------------------------------------------------------------
    Treats expr as a math expression and evaluates it.
    expr must have the following format:
        operand1 operator operand2
    operators are: +, -, *, /, %
    operands are one-digit integer numbers
    use: result = calculate(expr)
    -----------------------------------------------------------------
    Parameters:
        expr - an arithmetic expression to be calculated (str)
    Returns:
        result - The result of arithmetic expression (float)
    -----------------------------------------------------------------
    """
    expression = expr.split(" ")
    operand1 = expression[0]
    operator = expression[1]
    operand2 = expression[2]
    
    if operator == "+":
        return int(operand1) + int(operand2)
    if operator == "-":
        return int(operand1) - int(operand2)
    if operator == "*":
        return int(operand1) * int(operand2)
    if operator == "/" and operand2 != 0:
        return int(operand1) / int(operand2)
    if operator == "%":
        return int(operand1) % int(operand2)
    