"""
-------------------------------------------------------
Lab 10, Task 4
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2023-11-21"
-------------------------------------------------------
"""
# Imports
from functions import customer_first
# Constants


fh = open("customers.txt", "r", encoding="utf-8")
print(customer_first(fh))
fh.close()