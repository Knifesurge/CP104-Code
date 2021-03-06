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
def file_head(fh, n):
    """
    -------------------------------------------------------
    Prints first n lines of fh. Line numbering starts at 0.
    Use: file_head(fh, n)
    -------------------------------------------------------
    Parameters:
        fh - file to print (file - open for reading)
        n - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    fh.seek(0)
    line_num = 0
    while line_num < n:
        line = fh.readline()
        print(line, end='')
        line_num += 1
    return

def number_lines(fh_in, fh_out):
    """
    -------------------------------------------------------
    Adds line numbers to a file. Contents of fh_out contain contents
    of fh_in where every line has line numbers added to the beginning
    of the line in the format [number]. Line numbering starts at 0.
    Put a single space after the line number.
    Use: number_lines(fh_in, fh_out)
    -------------------------------------------------------
    Parameters:
        fh_in - file to read (file - open for reading)
        fh_out - file to write (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """
    fh_in.seek(0)
    fh_out.seek(0)
    fh_in_contents = fh_in.readlines()
    
    line_num = 0
    for line in fh_in_contents:
        new_line = "[" + str(line_num) + "] " + line
        fh_out.write(new_line)
        line_num += 1
    """
    for line_num, line in enumerate(fh_in_contents):
        new_line = "[" + line_num + "] " + line
        fh_out.write(new_line)
    """
    return

def get_addresses(fh):
    """
    -------------------------------------------------------
    Reads a addresses from fh into a list of addresses.
    Addresses are stored in fh in the form:
        forename
        surname
        street
        city
        --
    Each address in the list of addresses is a list of the form:
    [forename, surname, street, city]
    Use: addreses = get_addresses(fh)
    -------------------------------------------------------
    Parameters:
        fh - the address file (file - open for reading)
    Returns:
        addresses - the addresses from fh (str)
    -------------------------------------------------------
    """
    fh.seek(0)
    file_contents = fh.readlines()
    addresses = [[] for i in range(len(file_contents[0]))]
    
    address_num = 0
    for line in file_contents:
        if line.strip() == "--":
            address_num += 1
        else:
            addresses[address_num].append(line.strip())
    return addresses

def merge_letters(fh_letter, fh_addresses, fh_merged):
    """
    -------------------------------------------------------
    Merges a letter with a list of addresses.
    Writes the results to a file of completed letters.
    Use: merge_letters(fh_letter, fh_addresses, fh_merged)
    -------------------------------------------------------
    Parameters:
        fh_letter - a file with a letter to process (file - open for reading)
        fh_addresses - a file of addresses (file - open for reading)
        fh_merged - a file of merged letters (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """
    addresses = get_addresses(fh_addresses)
    fh_letter.seek(0)
    letter_contents = fh_letter.readlines()
    
    address_num = 0
    for i in range(len(addresses) - 1):
        for line in letter_contents:
            words = line.strip().split(" ")
            for word in words:
                #print(word)
                if "[forename]" in word:
                    fh_merged.write(addresses[address_num][0])
                    if word != "[forename]":
                        fh_merged.write(word[10:])
                elif "[surname]" in word:
                    fh_merged.write(addresses[address_num][1])
                    if word != "[surname]":
                        fh_merged.write(word[8:])
                elif "[street]" in word:
                    fh_merged.write(addresses[address_num][2])
                    if word != "[street]":
                        fh_merged.write(word[8:])
                elif "[city]" in word:
                    fh_merged.write(addresses[address_num][3])
                    if word != "[city]":
                        fh_merged.write(word[6:])
                else:
                    fh_merged.write(word)
                fh_merged.write(" ")
            fh_merged.write("\n")
        address_num += 1
    return

def student_info(students):
    """
    -------------------------------------------------------
    Get information from a file of students and grades.
    Use: l_id, h_id, avg = student_info(students)
    -------------------------------------------------------
    Parameters:
        students - student information file in the format
            surname,forename,id,mark (file - open for reading)
    Returns:
        l_id - the id of the student with the lowest mark (str)
        h_id - the id of the student with the highest mark (str)
        avg - the average mark (float)
    -------------------------------------------------------
    """
    students.seek(0)
    file_contents = students.readlines()
    ID_INDEX = 2
    GRADE_INDEX = 3
    ID_START = 11
    ID_END = 19 + 1
    GRADE_START = 21
    lowest_mark = file_contents[0][GRADE_START:]
    lowest_id = file_contents[0][ID_START:ID_END]
    highest_mark = file_contents[0][GRADE_START:]
    highest_id = file_contents[0][ID_START:ID_END]
    grade_total = 0
    
    for line in file_contents:
        entries = line.split(",")
        if entries[GRADE_INDEX] < lowest_mark:
            lowest_mark = entries[GRADE_INDEX]
            lowest_id = entries[ID_INDEX]
        if entries[GRADE_INDEX] > highest_mark:
            highest_mark = entries[GRADE_INDEX]
            highest_id = entries[ID_INDEX]
        grade_total += int(entries[GRADE_INDEX])
        
    avg = grade_total / len(file_contents)
    return lowest_id, highest_id, avg

def substitute(fh_in, fh_out, ciphertext):
    """
    -------------------------------------------------------
    Encipher a file using the letter positions in ciphertext.
    Only letters are enciphered, and the resulting strings are
    in upper case.
    Use: substitute(fh_in, fh_out, ciphertext)
    -------------------------------------------------------
    Parameters:
        fh_in - input file (file - open for reading)
        fh_out - output file (file - open for writing)
        ciphertext - ciphertext alphabet (str)
    Returns:
        None
    -------------------------------------------------------
    """
    fh_in.seek(0)
    file_contents = fh_in.readlines()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for line in file_contents:
        line_upper = line.upper()
        for letter in line_upper:
            if letter in alphabet:  # Only replacing letters
                for i in range(len(alphabet)):
                    char = alphabet[i]
                    if letter == char:
                        fh_out.write(ciphertext[i])
                        break
            else:
                fh_out.write(letter)
    return
                
def shift(fh_in, fh_out, n):
    """
    -------------------------------------------------------
    Encipher a file using a shift cipher.
    Only letters are enciphered, and the resulting strings are
    in upper case.
    Use: shift(fh_in, fh_out, n)
    -------------------------------------------------------
    Parameters:
        fh_in - input file (file - open for reading)
        fh_out - output file (file - open for writing)
        n - the number of letters to shift (int)
    Returns:
        None
    -------------------------------------------------------
    """
    fh_in.seek(0)
    file_contents = fh_in.readlines()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for line in file_contents:
        line_upper = line.upper()
        for letter in line_upper:
            if letter in alphabet:  # Only replacing letters
                for i in range(len(alphabet)):
                    char = alphabet[i]
                    if letter == char:
                        to_shift = i + n
                        #print("Letter: {}\ti: {}\tShift: {}".format(letter, i, to_shift), end='')
                        if to_shift > len(alphabet):
                            extra = to_shift - len(alphabet)
                            #print("\nExtra: {}".format(extra), end='')
                            if extra > 0:
                                to_shift = extra - 1
                            else:
                                to_shift = extra
                        elif to_shift == len(alphabet):
                            to_shift = 0
                        shift = alphabet[to_shift]
                        #print("\tNew Letter: {}".format(shift))
                        fh_out.write(shift)
                        break
            else:
                fh_out.write(letter)
    return
