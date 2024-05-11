"""
-------------------------------------------------------
Assignment 3, Task 3
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2023-10-18"
-------------------------------------------------------
"""
# Imports
from functions import extract_date
# Constants

def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """
    
year, month, day = extract_date(19621025)
print(f"({year:04d}, {month:02d}, {day:02d})")