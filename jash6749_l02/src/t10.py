"""
-------------------------------------------------------
Lab 2, Task 10
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
    
CHARGE = float(input('Food Charge: $'))
TAX = float(input('Sales Tax in (%): '))
TIP = float(input('Tip in (%): '))

tax_amount = (TAX/100)*CHARGE
tip_amount = (TIP/100)*CHARGE
total_bill = CHARGE+tax_amount+tip_amount

print('Cost of meal:')
print(f"{'Subtotal: $'}{CHARGE}")
print(f"{' ':<5}{'Tax: $'}{tax_amount}")
print(f"{' ':<5}{'Tip: $'}{tip_amount}")
print('------------------')
print(f"{' ':<3}{'Total: $'}{total_bill}")
