"""
-------------------------------------------------------
Lab 7, Task 8
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2023-10-30"
-------------------------------------------------------
"""
# Imports
from functions import budget
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
    
expenses, balance, status = budget(200)
print(f"{expenses:.2f}, {balance:.2f}, {status}")