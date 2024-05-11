"""
LAB 4, TASK 8
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2023-09-28"
-------------------------------------------------------
"""
# Imports
from functions import computer_costs
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
    
pre_comm, total_cost = computer_costs(1399, 87, 8.5)
print(f"({pre_comm:.2f}, {total_cost:.2f})")