"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2018-11-22
------------------------------------------------------------------------
"""
from random import randint, uniform

def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """
    matrix = [[0 for col in range(cols)] for row in range(rows)]    # Create a new empty 2d array of the required size
    for row in range(rows):
        for col in range(cols):
            if value_type == "float":
                matrix[row][col] = uniform(low, high)
            else:   # value_type == "int"
                matrix[row][col] = randint(low, high)
                
    return matrix

def generate_matrix_char(rows, cols):
    """
    -------------------------------------------------------
    Generates a 2D list of random character values
    Use: matrix = generate_matrix_char(rows, cols)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the generated matrix (int > 0)
        cols - number of columns in the generated matrix (int > 0)
    Returns:
        matrix - a 2D list of random characters (2D list of str)
    -------------------------------------------------------
    """
    matrix = [[0 for col in range(cols)] for row in range(rows)]
    chars = "abcdefghijklmnopqrstuvwxyz"
    for row in range(rows):
        for col in range(cols):
            random_num = randint(0, len(chars))
            matrix[row][col] = chars[random_num]
    return matrix

def matrix_distinct_values(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of  unique numbers of type float or int.
    Use: matrix = matrix_distinct_values(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of unique values (list of int/float)
    -------------------------------------------------------
    """
    matrix = [[0 for col in range(cols)] for row in range(rows)]
    nums_used = []
    random_num = 0
    for i in range(rows):
        for j in range(cols):
            if value_type == "float":
                while random_num in nums_used:
                    random_num = uniform(low, high)
                nums_used.append(random_num)
                matrix[i][j] = random_num
            else:   # value_type == "int:
                while random_num in nums_used:
                    random_num = randint(low, high)
                nums_used.append(random_num)
                matrix[i][j] = random_num
    return matrix

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

def print_matrix_char(matrix):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list of strings in a formatted table.
    Prints row and column headings.
    Use: print_matrix_char(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of strings (2D list)
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
            print("{:>6s}".format(matrix[i][j]), end='')
            
def words_to_matrix(word_list):
    """
    -------------------------------------------------------
    Generates a 2D list of character values from the given
    list of words. All words must be the same length.
    Use: matrix = words_to_matrix(word_list)
    -------------------------------------------------------
    Parameters:
        word_list - a list containing the words to be placed in
            the matrix (list of string)
    Returns:
        matrix - a 2D list of characters of the given words
         in word_list (2D list of string).
    -------------------------------------------------------
    """
    matrix = [["" for col in range(len(word_list[0]))] for row in range(len(word_list))]
    index1 = 0
    index2 = 0
    for word in word_list:
        for char in word:
            matrix[index1][index2] = char
            index2 += 1
        index1 += 1
        index2 = 0
    return matrix

def stats(matrix):
    """
    -------------------------------------------------------
    Returns statistics on a 2D list.
        Use: smallest, largest, total, average = stats(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list of float/int)
    Returns:
        smallest - the smallest number in matrix (float/int)
        largest - the largest number in matrix (float/int)
        total - the total of the numbers in matrix (float/int)
        average - the average of numbers in matrix (float/int)
    -------------------------------------------------------
    """
    smallest = matrix[0][0]
    largest = matrix[0][0]
    total = 0
    count = 0
    for row in matrix:
        for val in row:
            if val < smallest:
                smallest = val
            if val > largest:
                largest = val
            total += val
            count += 1
            
    average = total / count
    return smallest, largest, total, average

def find_position(matrix):
    """
    -------------------------------------------------------
    Determines locations [row, column] of smallest and largest
    values in a 2D list.
    Use: s_loc, l_loc = find_position(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list)
    Returns:
        s_loc - a list of of the row and column location of
            the smallest value in matrix (list of int)
        l_loc - a list of of the row and column location of
            the largest value in matrix (list of int)
    -------------------------------------------------------
    """
    smallest = matrix[0][0]
    largest = matrix[0][0]
    s_loc = []
    l_loc = []
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            val = matrix[i][j]
            if val < smallest:
                smallest = val
                s_loc.insert(0, i)
                s_loc.insert(1, j)
            if val > largest:
                largest = val
                l_loc.insert(0, i)
                l_loc.insert(1, j)
    return s_loc, l_loc

def find_less(matrix, n):
    """
    -------------------------------------------------------
    Finds the location [row, column] of the first value in matrix
    that is smaller than a target value, n. If there is no such
    number in matrix, it should return an empty list.
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list)
        n - the target value (float)
    Returns:
        loc - a list of the row and column location of
            the the first value smaller than n in values,
            an empty list otherwise (list of int)
    -------------------------------------------------------
    """
    loc = []
    
    sentinel = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            val = matrix[i][j]
            while sentinel == 0:
                if val < n:
                    sentinel += 1
                    loc.extend([i, j])
    return loc

def count_frequency(matrix, c):
    """
    -------------------------------------------------------
    Count the number of appearances of the given character c
    in matrix.
    Use: count = count_frequency(matrix, c)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to search in it (2D list of str)
        c - character to search for it (str, len = 1)
    Returns:
        count - the number of appearances of c in the matrix (int)
    -------------------------------------------------------
    """
    count = 0
    
    for row in matrix:
        for char in row:
            if char == c:
                count += 1
                
    return count
            
def find_word_horizontal(matrix, word):
    """
    -------------------------------------------------------
    Look for word in each row of the given matrix of characters.
    Returns a list of indexes of all rows that are equal to word.
    Returns an empty list if no row is equal to word.
    Use: rows = find_word_horizontal(matrix, word)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix of characters (2D list of str)
        word - the word to search for (str)
    Returns:
        rows - a list of row indexes (list of int)
    ------------------------------------------------------
    """
    rows = []

    index = 0
    for row in matrix:
        row_word = "".join(row)
        if row_word == word:
            rows = index
        index += 1
    return rows

def find_word_vertical(matrix, word):
    """
    -------------------------------------------------------
    Look for word in each column of the given matrix of characters.
    Returns a list of indexes of all column that are equal to word.
    Returns an empty list if no column is equal to word.
    Use: cols = find_word_vertical(matrix, word)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix of characters (2D list of str)
        word - the word to search for (str)
    Returns:
        cols - a list of column indexes (list of int)
    ------------------------------------------------------
    """
    cols = []
    index = 0
    for row in matrix:
        for col in row:
            pass
    return

def find_word_diagonal(matrix, word):
    """
    -------------------------------------------------------
    Returns whether word is on the diagonal of a square matrix
    of characters.
    Use: found = find_word_diagonal(matrix, word)
    -------------------------------------------------------
    Parameters:
        matrix - a 2d list of characters (2d list of str)
        word - the word to compare against the diagonal of matrix (str)
    Returns:
        found - True if word is on the diagonal of matrix,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    diagonal = []
    found = False
    for i in range(len(matrix)):
        diagonal.append(matrix[i][i])
    
    diagonal_word = "".join(diagonal)
    if word == diagonal_word:
        found = True
    return found

def scalar_multiply(matrix, num):
    """
    -------------------------------------------------------
    Update matrix by multiplying each element of matrix by num.
    Use: scalar_multiply(matrix, num)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to multiply (2D list of int/float)
        num - the number to multiply by (int/float)
    Returns:
        None
    ------------------------------------------------------
    """
    for row in matrix:
        for val in row:
            val *= num
    return

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

def matrix_equal(matrix1, matrix2):
    """
    -------------------------------------------------------
    Compares two matrices to see if they are equal - i.e. have the
    same contents in the same locations.
    Use: equal = matrix_equal(matrix1, matrix2)
    -------------------------------------------------------
    Parameters:
        matrix1 - the first matrix (2D list of ?)
        matrix2 - the second matrix (2D list of ?)
    Returns:
        equal - True if matrix1 and matrix2 are equal,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    equal = False
    
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            val1 = matrix1[i][j]
            val2 = matrix2[i][j]
            if val1 == val2:
                equal = True
            else:
                equal = False
                break;
    return equal
