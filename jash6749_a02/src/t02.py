"""
-------------------------------------------------------
Assignment 2, Task 2
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
    
num = int(input("Enter a positive digit number: "))

num_a = int((num/10) // 1)
num_b = int((round((num/10) % 1, 2))*10)

diff = num_a - num_b

print(f"The difference of the digits of {num} is {diff}")