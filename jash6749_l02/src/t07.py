"""
-------------------------------------------------------
Lab 2, Task 7
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

FLYERS = int(input('Number of flyers: '))
VOLUNTEERS = int(input('Number of volunteers: '))

each_flyers = FLYERS//VOLUNTEERS
leftover = FLYERS%VOLUNTEERS

print('Flyers per volunteer: ', each_flyers)
print('Flyers left over: ', leftover)