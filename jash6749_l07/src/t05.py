"""
-------------------------------------------------------
Lab 7, Task 5
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2023-10-30"
-------------------------------------------------------
"""
# Imports
from functions import positive_statistics
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
mini, maxi, total, average = positive_statistics()
print(f"{mini:.2f}, {maxi:.2f}, {total:.2f}, {average:.2f}")