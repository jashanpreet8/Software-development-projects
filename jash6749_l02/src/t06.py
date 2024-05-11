"""
-------------------------------------------------------
Lab 2, Task 6
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2023-09-18"
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
    
PRINCIPAL = float(input('Mortgage principal ($): '))
YEARS = int(input('Number of years: '))
INTEREST = float(input('Yearly interest rate (%): '))

months = YEARS*12
monthly_interest = (INTEREST/100)/12

monthly_payment = PRINCIPAL*((monthly_interest*((1+monthly_interest)**months))/(((1+monthly_interest)**months)-1))

print('The monthly payments are: $', monthly_payment)