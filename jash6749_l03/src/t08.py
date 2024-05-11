"""
-------------------------------------------------------
Lab3, Task 8
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2023-09-25"
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
    
dirt = float(input('Enter amount of dirt (m^3): '))
gravel = float(input('Enter amount of gravel (m^3): '))
sand = float(input('Enter amount of sand (m^3): '))

total = dirt+gravel+sand

print('Material    Cubic Meters')
print(f"Dirt        {dirt:6.1f}")
print(f"Gravel      {gravel:5.1f}")
print(f"Sand        {sand:5.1f}")
print(f"Total       {total:5.1f}")