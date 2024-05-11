"""
-------------------------------------------------------
Assignment 2, Task 4
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
    
flyers = int(input("Number of flyers: "))
people = int(input("Number of delivery people: "))

flyers_each = flyers // people
flyers_left = flyers % people

print("Flyers per delivery person:", flyers_each)
print("Flyers left over:", flyers_left)