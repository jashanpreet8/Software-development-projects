"""
-------------------------------------------------------
Lab 10, Task 7
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2023-11-21"
-------------------------------------------------------
"""
# Imports
from functions import append_max_num
# Constants

fh = open("numbers.txt", "r+", encoding="utf-8")
print(f'{append_max_num(fh)} is appended')
fh.close()
