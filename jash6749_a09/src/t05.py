"""
-------------------------------------------------------
Assignment 9, Task 5
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2023-12-01"
-------------------------------------------------------
"""
# Imports
from functions import student_stats
# Constants

fh = open('students.txt', 'r', encoding='utf-8')
l_id, h_id, avg = student_stats(fh)
fh.close()

print(f"{l_id}, {h_id}, {avg}")