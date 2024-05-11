"""
-------------------------------------------------------
Assignment 9, Task 2
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2023-12-01"
-------------------------------------------------------
"""
# Imports
from functions import read_integers
# Constants

fh = open('numbers.txt', 'r', encoding='utf-8')
print(read_integers(fh))
fh.close()