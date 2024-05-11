"""
-------------------------------------------------------
Lab 10, Task 11
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2023-11-21"
-------------------------------------------------------
"""
# Imports
from functions import find_longest
# Constants

fh = open("words.txt", "r", encoding="utf-8")
word = find_longest(fh)
fh.close()

print(f"'{word}' is the last longest word")