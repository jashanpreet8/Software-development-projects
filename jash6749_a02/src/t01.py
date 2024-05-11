"""
-------------------------------------------------------
Assignment 2, Task 1
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2023-09-30"
-------------------------------------------------------
"""
# Imports

# Constants
TAX = 18.50

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
    
sales = float(input("Enter the total sales: $"))

tax_amount = TAX*sales/100

print("Projected Tax Report")
print("--------------------------")
print(f"Total sales:   $ {sales:,.2f}")
print(f"Annual tax:    % {TAX}")
print("--------------------------")
print(f"Tax:           $  {tax_amount:,.2f}")