"""
-------------------------------------------------------
Assignment 2, Task 3
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2023-09-30"
-------------------------------------------------------
"""
# Imports

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
    
date = int(input("Enter a date in the format YYYYMMDD: "))

year = date//10000
date_left = date%10000
month = date_left//100
day = date_left%100

print(f"The reformatted date: {year:04d}/{month:02d}/{day:02d}")