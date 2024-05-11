"""
-------------------------------------------------------
Assignment 9, Task 4
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2023-12-01"
-------------------------------------------------------
"""
# Imports
from functions import line_numbering
# Constants

fr = open('wilde.txt', 'r', encoding='utf-8')
fw = open('wilde_numbered.txt', 'w', encoding='utf-8')

line_numbering(fr, fw)

fr.close()
fw.close()