"""
-------------------------------------------------------
Lab 10, Task 13
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2023-11-21"
-------------------------------------------------------
"""
# Imports
from functions import file_copy
# Constants

fh_1 = open("words.txt", "r", encoding="utf-8")
fh_2 = open("new_words.txt", "w", encoding="utf-8")
file_copy(fh_1, fh_2)
fh_1.close()
fh_2.close()

print(f"Copying 'words.txt' to 'new_words.txt'")