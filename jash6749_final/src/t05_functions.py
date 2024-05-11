"""
-------------------------------------------------------
Exam Task 5 Function Definitions
-------------------------------------------------------
Author: Jashanpreet Singh Jashanpreet Singh
ID:     169046749
Email:  jash6749@mylaurier.ca
__updated__ = "2023-12-13"
-------------------------------------------------------
"""


def fill_matrix(fh_in, rows, cols):
    """
    -------------------------------------------------------
    Creates a rows by cols 2D list of integers filled with
    space-separated integers from f_in. If f_in does not have enough values,
    fill the remaining slots with 0s. If f_in has too many values,
    the excess values are ignored.
    Use: matrix = fill_matrix(fh_in, rows, cols)
    -------------------------------------------------------
    Parameters:
        fh_in - the integers file to process (file handle - already open for reading)
        rows - rows in matrix (int > 0)
        cols - columns in matrix (int > 0)
    Returns‌​‌​​​​‌​​‌‌​‌‌‌​​‌​‌‌​‌‌‌​‌:
        matrix - a 2D list of integers (2D list of int)
    -------------------------------------------------------
    """

    # Your code here
    list = []
    line = fh_in.readline()
    
    while line != '':
        ints = line.split()
        i = 0
        for row in range(rows):
            il = []
            for col in range(cols):               
                if i < len(ints):
                    il.append(int(ints[i]))
                    i += 1
                else:
                    line = fh_in.readline()
                    if line == '':
                        il.append(0)
                    else:
                        ints = line.split()
                        i = 0
                        il.append(int(ints[i]))
                        i += 1
            list.append(il)
        break
            
    return list
