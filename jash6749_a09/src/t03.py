"""
-------------------------------------------------------
Assignment 9, Task 3
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2023-12-01"
-------------------------------------------------------
"""
# Imports
from functions import file_statistics
# Constants

fh = open('addresses.txt', 'r', encoding='utf-8')
uc, lc, dc, wc, rc = file_statistics(fh)
fh.close()

print(f"{uc}, {lc}, {dc}, {wc}, {rc}")