"""
-------------------------------------------------------
Assignment 9, Task 1
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2023-12-01"
-------------------------------------------------------
"""
# Imports
from functions import file_top
# Constants

fh = open('students.txt', 'r', encoding='utf-8')
file_top(fh, 20)
fh.close()