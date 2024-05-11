"""
-------------------------------------------------------
Lab 11, Functions
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2023-11-30"
-------------------------------------------------------
"""
# Imports
from random import randint, uniform
# Constants
    
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
    matrix = []
    
    if value_type == 'int':
        for row in range(rows):
            strip = []
            for col in range(cols):
                strip.append(randint(low, high))
            matrix.append(strip)
                
    elif value_type == 'float':
        for row in range(rows):
            strip = []
            for col in range(cols):
                strip.append(uniform(low, high))
            matrix.append(strip)
                
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
    hor = 0
    ver = 0
    
    print(' ', end='')
    length = len(matrix[0])
    for l in range(length):
        print(f"{ver:>7}", end='')
        ver += 1
    print()
    
    if value_type == 'int':
        for row in matrix:
            print(hor, end='')
            hor += 1
            for value in row:
                print(f"{value:>7}", end = '')
            print()
            
    elif value_type == 'float':
        for row in matrix:
            print(hor, end='')
            hor += 1
            for value in row:
                print(f"{value:>7.2f}", end = '')
            print()
    
    return None
    
def matrix_stats(matrix):
    """
    -------------------------------------------------------
    Returns statistics on a 2D list.
        Use: smallest, largest, total, average = matrix_stats(matrix)
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
    sm, lar = matrix[0][0], matrix[0][0] 
    tot, cou = 0, 0
    
    for row in matrix:
        for value in row:
            if value < sm:
                sm = value
            if value > lar:
                lar = value
            tot += value
            cou += 1
            
    avg = tot/cou 
    
    return sm, lar, tot, avg
    
def find_less(matrix, n):
    """
    -------------------------------------------------------
    Finds the location [row, column] of the first value in matrix
    that is smaller than a target value, n. If there is no such
    number in matrix, it should return an empty list.
    Use: loc = find_less(matrix, n)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list)
        n - the target value (float)
    Returns:
        loc - a list of the row and column location of
            the first value smaller than n in values,
            an empty list otherwise (list of int)
    -------------------------------------------------------
    """
    list = []
    found = False
    i = 0
    
    while i < len(matrix[0]) and not found:
        j = 0
        while j < len(matrix[i]) and not found:
            if matrix[i][j] < n:
                list.append(i)
                list.append(j) 
                found = True
            j += 1
        i += 1     
                
    return list
            
    
def matrix_scalar_multiply(matrix, num):
    """
    -------------------------------------------------------
    Update matrix by multiplying each element of matrix by num.
    Use: matrix_scalar_multiply(matrix, num)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to multiply (2D list of int/float)
        num - the number to multiply by (int/float)
    Returns:
        None
    ------------------------------------------------------
    """
    for row in matrix:
        for value in range(len(row)):
            row[value] *= num
    return None
    