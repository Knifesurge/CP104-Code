"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-27
------------------------------------------------------------------------
"""
from cereal_data import COLUMNS
"""
======================================================
Imported from Lab 10
======================================================
"""
def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        None.
    -------------------------------------------------------
    """
    print("{:>4}".format(""),end='')
    for i in range(len(matrix[0])):
        print("{:>6}".format(i), end='')
    
    for i in range(len(matrix)):
        print()
        print("{:>4d}".format(i),end='')
        for j in range(len(matrix[i])):
            if value_type == "float":
                print("{:>6.2f}".format(matrix[i][j]), end='')
            else:
                print("{:>6d}".format(matrix[i][j]), end='')

def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of ?)
    Returns:
        b - the transposed matrix (2D list of ?)
    ------------------------------------------------------
    """
    # Tranposed matrix
    b = [[0 for row in range(len(a))] for col in range(len(a[0]))]
    
    for i in range(len(a[0])):
        for j in range(len(a)):
            b[i][j] = a[j][i]
    return b

"""
======================================================
"""

def binary_search(values, key):
    """
    -------------------------------------------------------
    Searches for the first occurrence of key in the sorted list
    values. Returns -1 if key is not found.
    Use: i = binary_search(values, key)
    -------------------------------------------------------
    Parameters:
        values - a list of data (sorted list of ?)
        key - a data element (?)
    Returns:
        i - the index of the first occurrence of key in
            the list, -1 if key is not found. (int)
    -------------------------------------------------------
    """
    i = -1
    lower = 0   # Lower bound to search
    upper = len(values) # Upper bound to search
    found = False
    while lower < upper and not found:
        i = lower + (upper - lower) // 2    # Compute i for this pass
        val = values[i] # Value to check
        if key > val: # Have to search 'right side' of list
            if lower == i:
                break;
            lower = i
        elif key <= val: # Have to search 'left side' of list
            upper = i
        elif key == val:  # Break if equal
            found = True
    if i == 0 and values[i] != key:
        i += 1
    return i

def flatten(values):
    """
    -------------------------------------------------------
    Flattens a 2D list. Creates a new 1D list from values.
    Use: flattened = flatten(values)
    -------------------------------------------------------
    Parameters:
        values - a 2D list of data (list of list of ?)
    Returns:
        flattened - a 1D list of flattened values (list ?)
    -------------------------------------------------------
    """
    flattened = []
    
    for row in values:
        for val in row:
            flattened.append(val)
    return flattened

def matrix_multiply(a, b):
    """
    -------------------------------------------------------
    Multiplies a by b. Matrices are multiplied by taking the dot product
    of the rows of a against the columns of b.
    Rows of a == columns of b, columns of a == rows of b.
    See: https://en.wikipedia.org/wiki/Matrix_multiplication
    Use: c = matrix_multiply(a, b)
    -------------------------------------------------------
    Parameters:
        a - the matrix to multiply (2D list of int/float)
        b - the matrix to multiply by (2D list of int/float)
    Returns:
        c - the resulting matrix of a times b
            (2D list of int/float)
    ------------------------------------------------------
    """
    c = [[0 for col in range(len(b[0]))] for row in range(len(a))]  # Create a new list of size a.rows x b.cols

    # Loop through rows of a
    for i in range(len(a)):
        # Loop through columns of b:
        for j in range(len(b[i])):
            # Loop through rows of b:
            for n in range(len(b)):
                c[i][j] += a[i][n] * b[n][j]
    return c

def pig_latin(word):
    """
    -------------------------------------------------------
    Converts a word to Pig Latin. The conversion is:
    - if a word begins with a vowel, add "way" to the end of the word.
    - if the word begins with consonants, move all consonants to the
    end of the word and add "ay" to the end of that.
    "y" is treated as a consonant if it is the first character in the word,
    and as a vowel for anywhere else in the word.
    Preserve the case of the word - i.e. if the first character of word
    is upper-case, then the new first character should also be upper case.
    Use: pl = pig_latin(word)
    -------------------------------------------------------
    Parameters:
        word - a string to convert to Pig Latin (str)
    Returns:
        pl - the Pig Latin version of word (str)
    ------------------------------------------------------
    """
    VOWELS = "aeiouAEIOU"
    CONSONANTS = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
#    STARTING_CONSONANTS = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    pl = list(word)    # Create a list representation of the word
    
    if pl[0] in VOWELS:   # Word begins with a vowel, so add way
        pl.append("way")
    else:   # Starts with a consonant
        # Grab the starting consonants...
        index = 0
        char = pl[index]
        if char in "Yy":
            index += 1
            char = pl[index]
        while char in CONSONANTS:
            index += 1
            char = pl[index]
        # Index now the index of last starting consonant
        # Move beginning consonants to end of word
        begin = word[:index]
        pl.append(begin)
        # Remove the beginning consonants
        for i in range(index):
            del pl[0]
        # Add 'ay' to the end
        pl.append("ay")
    
    # Maintain capitalization
    for i in range(len(pl)):
        pl[i] = pl[i].lower()
    if word[0].isupper():
        pl[0] = pl[0].upper()
    
    return "".join(pl)

# Task 5
def read_cereals(fh):
    """
    -------------------------------------------------------
    Reads cereal data from a file into a 2D list of cereal data.
    See: cereal_data.py for column names and information.
    'shelf' and 'vitamin' columns must be converted to int.
    'calories' through 'cups' columns must be converted to float.
    Use: cereals = read_cereals(fh)
    -------------------------------------------------------
    Parameters:
        fh - file handle for cereal data (file - open for reading)
    Returns:
        cereals - a 2D list of cereal data (list of ?)
    ------------------------------------------------------
    """
    fh.seek(0)
    lines = fh.readlines()
    cereals = [[] for line in range(len(lines))]
    
    # Load all lines into the cereals 2D list
    index = 0
    for line in lines:
        # Removes trailing comma and newline
        cereals[index] = line[:-1].strip().split(",")
        index += 1
    
    calories_passed = False
    # Process some columns
    for i in range(len(cereals)):
        for j in range(len(cereals[i])):
            current_column = COLUMNS[j]
            if current_column == "calories":
                calories_passed = True
            elif current_column == "shelf":
                cereals[i][j] = int(cereals[i][j])
            elif current_column == "vitamins":
                cereals[i][j] = int(cereals[i][j])
            # Convert 'calories' -> 'cups' (end of list) to float
            if calories_passed:
                cereals[i][j] = float(cereals[i][j])
        calories_passed = False
            
    return cereals

def cereals_by_value(cereals, column, value):
    """
    -------------------------------------------------------
    Returns the rows of cereals where column value == value.
    Use: data = cereals_by_value(cereals, column, value)
    -------------------------------------------------------
    Parameters:
        cereals - a 2D list of cereal data (list of ?)
        column - a column name (str)
        value - the value of column in a row (str)
    Returns:
        some_cereals - a 2D list of cereal data (list of ?)
    ------------------------------------------------------
    """
    temp_cereals = [[] for i in range(len(cereals))]
    
    index = 0
    for i in range(len(cereals)):
        for j in range(len(cereals[i])):
            column_value = COLUMNS[j]
            cereals_value = cereals[i][j]
            if column_value == column:
                if cereals_value == value:
                    temp_cereals[index] = cereals[i]
                    index += 1
                    
    # Remove empty lists and set some_cereals = temp_cereals
    some_cereals = [i for i in temp_cereals if i != []]
    
    return some_cereals

def cereal_stats(cereals, columns):
    """
    -------------------------------------------------------
    Calculates and returns the minimum, maximum, count, total, and
    average of the values in each column of columns.
    Use: data = cereal_stats(cereals, columns)
    -------------------------------------------------------
    Parameters:
        cereals - a 2D list of cereal data (list of ?)
        columns - a list of column names (list of str)
    Returns:
        data - a dictionary of stats values in the form
            {column: [minimum, maximum, count, total, average]}
            (dict of string: list of int/float)
    ------------------------------------------------------
    """
    NUM_DATA_ENTRIES = 5    # Min, Max, Count, Total, Avg
    data = {"DELETEME": 0}
    minimum = 1000  # Arbitrary large number
    MIN_INDEX = 0   # Index of minimum value
    maximum = 0 # Arbitrary small number
    MAX_INDEX = 1   # Index of maximum value
    count = 0
    COUNT_INDEX = 2 # Index of count value
    total = 0
    TOTAL_INDEX = 3 # Index of total value
    AVG_INDEX = 4   # Index of avg value
    # Loop over cereals
    for i in range(len(cereals)):
        # Loop over entries in cereal
        for j in range(len(cereals[i])):
            # Column name
            column_value = COLUMNS[j]
            # Value at column name
            cereals_value = cereals[i][j]
            # Do we want the current column?
            if column_value in columns:
                # Key not present in dict, create it
                if column_value not in data.keys():
                    data[column_value] = [0 for i in range(NUM_DATA_ENTRIES)]
                    print("{} : {}".format(column_value, data[column_value]))
                if cereals_value < data[column_value][MIN_INDEX]:
                    data[column_value][MIN_INDEX] = cereals_value
                if cereals_value > data[column_value][MAX_INDEX]:
                    data[column_value][MAX_INDEX] = cereals_value
                data[column_value][TOTAL_INDEX] += cereals_value
                data[column_value][COUNT_INDEX] += 1
    
    # Delete first entry of dict (key = "DELETEME")
    del data["DELETEME"]
    # Calculate average for each column
    for key, value in data.items():
        value[AVG_INDEX] = value[TOTAL_INDEX] / value[COUNT_INDEX]
    return data

def cereal_stats_table(data):
    """
    -------------------------------------------------------
    Prints the values in stats_data in a tabular format. Titles are:
        Column      Minimum  Maximum    Count    Total  Average
        ---------- -------- -------- -------- -------- --------
    float values are printed with 1 decimal point.
    Use: cereal_stats_table(data)
    -------------------------------------------------------
    Parameters:
        stats_data - a dictionary of stats values in the form
            {column: [minimum, maximum, count, total, average]}
            (dict of string: list of int/float)
    Returns:
        None
    ------------------------------------------------------
    """
    print("{:<10s} {:>8s} {:>8s} {:>8s} {:>8s} {:>8s}".format("Column", "Minimum", "Maximum", "Count", "Total", "Average"))
    print("{:-<10s} {:->8s} {:->8s} {:->8s} {:->8s} {:->8s}".format("", "", "", "", "", ""))
    for key, value in data.items():
        print("{:<10s} {:>8.1f} {:>8.1f} {:>8} {:>8.1f} {:>8.1f}".format(key, value[0], value[1], value[2], value[3], value[4]))

    return

def to_gray(colour_pixel):
    """
    -------------------------------------------------------
    Converts a single 24-bit (3 byte) BMP colour_pixel to gray using:
    gray = 0.06 * red + 0.6 * green + 0.33 * blue
    Use: gray_pixel = to_gray(colour_pixel)
    -------------------------------------------------------
    Parameters:
        colour_pixel - a colour pixel (bytearray)
    Returns:
        gray_pixel - a gray pixel (bytearray)
    -------------------------------------------------------
    """
    blue = colour_pixel[0]
    green = colour_pixel[1]
    red = colour_pixel[2]
    
    gray = (0.06 * red) + (0.6 * green) + (0.33 * blue)
    colour_pixel[0] = int(gray)
    colour_pixel[1] = int(gray)
    colour_pixel[2] = int(gray)
    return colour_pixel

def grayscale(fh_colour, fh_gray):
    """
    -------------------------------------------------------
    Converts the 24-bit BMP image file fh_colour to grayscale and saves
    it in fh_gray.
    Use: grayscale(fh_colour, fh_gray)
    -------------------------------------------------------
    Parameters:
        fh_colour - the input BMP file variable (file - open for reading bytes)
        fh_gray - the output BMP file variable (file - open for writing bytes)
    Returns:
        None
    -------------------------------------------------------
    """
    # Read the 10th to 13th bytes of the header to get size
    fh_colour.seek(10)
    # Read the next 3 bytes
    bytes_read = fh_colour.read(3)
    # Size of header
    size = int.from_bytes(bytes_read, byteorder="little")
    # Jump to first byte after the header
    fh_colour.seek(0)
    # Write the header to the new file
    for i in range(size):
        bytes = fh_colour.read(1)
        fh_gray.write(bytes)
    fh_colour.seek(size)
    # Start reading in bytes
    # Read the first 3 bytes that make the first pixel
    bytes_read = fh_colour.read(3)
    while bytes_read != b'':
        list_of_bytes = bytearray(bytes_read)
        if len(list_of_bytes) != 3:
            break
        gray_pixel = to_gray(list_of_bytes)
        fh_gray.write(gray_pixel)
        bytes_read = fh_colour.read(3)
    return
