"""
-------------------------------------------------------
ASSIGNMENT 1, TASK 5
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2023-09-26"
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
    
p = float(input('Principal: $'))
r = float(input('Interest (%): '))
t = int(input('Number of years: '))
n = int(input('Number of times interest compounded per year: '))

r = r/100
amount = p*((1+(r/n))**(n*t))

print('Balance: $', amount)