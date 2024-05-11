"""
-------------------------------------------------------
Assignment 9, Functions
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2023-12-01"
-------------------------------------------------------
"""
# Imports

# Constants

def file_top(file_handle, count):
    """
    -------------------------------------------------------
    Prints first count lines of file_handle. Line numbering starts at 0.
    If length of file is shorter than count, stops printing after
    last line of file.
    Use: file_top(file_handle, count)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
        count - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    line = file_handle.readline()
    num = 0
    
    while num != count and line != '':
        print(line, end='')
        line = file_handle.readline()
        num += 1
        
    return None
    
def read_integers(file_handle):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: number_list = read_integers(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        number_list - a list of integers from file_handle (list of int)
    -------------------------------------------------------
    """
    list = []
    line = file_handle.readline()
    
    while line != '':
        line = line.replace('\n', '')
        values = line.split(',')
        for value in values:
            if value.isdigit() and int(value) > 0:
                list.append(int(value))
        line = file_handle.readline()
    
    return list
    
def file_statistics(file_handle):
    """
    -------------------------------------------------------
    Evaluates the contents of a file by counting upper-case letters,
    lower-case letters, digits, white-spaces (including end-of-line
    characters), and remaining characters.
    Use: ucount, lcount, dcount, wcount, rcount = file_statistics(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        ucount - The number of upper-case letters in the file (int)
        lcount - The number of lower-case letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of white-space characters in the file (int)
        rcount - The number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    line = file_handle.readline()
    uc, lc, dc, wc, rc = 0, 0, 0, 0, 0
    
    while line != '':
        for c in line:
            if c.isupper():
                uc += 1
            elif c.islower():
                lc += 1
            elif c.isdigit():
                dc += 1
            elif c in [' ', '\n']:
                wc += 1
            else:
                rc += 1
        line = file_handle.readline()
    
    return uc, lc, dc, wc, rc
    
def line_numbering(fh_read, fh_write):
    """
    -------------------------------------------------------
    Adds line numbers to a file. Contents of fh_write contain contents
    of fh_read where every line has line numbers added to the beginning
    of the line in the format [number]. Line numbering starts at 0.
    Put a single space after the line number.
    Use: line_numbering(fh_read, fh_write)
    -------------------------------------------------------
    Parameters:
        fh_read - file to read (file - open for reading)
        fh_write - file to write (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """
    line = fh_read.readline()
    num = 0
    
    while line != '':
        fh_write.write(f"[{num}] {line}")
        line = fh_read.readline()
        num += 1
    
    return None
    
def student_stats(file_handle):
    """
    -------------------------------------------------------
    Get information from a file of file_handle and grades.
    Use: l_id, h_id, avg = student_stats(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - student information file in the format
            surname,forename,id,mark (file - open for reading)
    Returns:
        l_id - the id of the student with the lowest mark (str)
        h_id - the id of the student with the highest mark (str)
        avg - the average mark (float)
    -------------------------------------------------------
    """
    line = file_handle.readline()
    line.replace('\n', '')
    values = line.split(',')
    count, total = 0, 0
    low, high = values[3], values[3]
    li, hi = values[2], values[2]
    
    while line != '':
        if values[3] < low:
            low = values[3]
            li = values[2]
        if values[3] > high:
            high = values[3]
            hi = values[2]
        total += int(values[3])    
        count += 1
        line = file_handle.readline()
        line.replace('\n', '')
        values = line.split(',')
    
    avg = total/count
    
    return li, hi, avg       