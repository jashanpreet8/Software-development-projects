"""
-------------------------------------------------------
Testing for Task 7: line_lengths
-------------------------------------------------------
Author: Jashanpreet Singh Jashanpreet Singh
ID:     169046749
Email:  jash6749@mylaurier.ca
__updated__ = "2023-08-25"
-------------------------------------------------------
"""
# Imports
from t07_functions import line_lengths
# your imports here

# Your code here
f_in = open('source.txt', 'r', encoding='utf-8')
f_short = open('f_short.txt', 'w', encoding='utf-8')
f_long = open('f_long.txt', 'w', encoding='utf-8')

print(line_lengths(f_in, f_short, f_long, 16))

f_in.close()
f_short.close()
f_long.close()

