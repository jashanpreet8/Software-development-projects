"""
-------------------------------------------------------
Lab 2, Task 1
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2023-09-16"
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

FREEZING = 32    
CELSIUS = int(input('Temperature(C): '))
fahrenheit = ((9/5)*CELSIUS) + 32.0

if fahrenheit == FREEZING:
    pass

print('Temperature(F):', fahrenheit)