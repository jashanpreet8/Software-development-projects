"""
-------------------------------------------------------
Lab 10, Task 10
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2023-11-21"
-------------------------------------------------------
"""
# Imports
from functions import count_frequency_word
# Constants

word = 'Exercise'

fh = open("words.txt", "r", encoding="utf-8")
number = count_frequency_word(fh, word)
fh.close()

print(f'Word to count: {word}')
print(f"'{word}' appears {number} time(s)")
