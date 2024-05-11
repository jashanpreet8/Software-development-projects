"""
-------------------------------------------------------
Exam Task 3 Function Definitions
-------------------------------------------------------
Author: Jashanpreet Singh Jashanpreet Singh
ID:     169046749
Email:  jash6749@mylaurier.ca
__updated__ = "2023-12-13"
-------------------------------------------------------
"""


def upper_vowels(string):
    """
    -------------------------------------------------------
    Converts vowels in a string to upper-case, all other 
    letters to lower-case. Non letters are left unchanged.
    Vowels include: aeiou.
    Use: altered = upper_vowels(string)
    -------------------------------------------------------
    Parameters:
        string - string to process (str)
    Returns‌​‌​​​​‌​​‌‌​‌‌‌​​‌​‌‌​‌‌‌​‌:
        altered - the resulting string (str)
    -------------------------------------------------------
    """

    # Your code here
    vowels = ['a', 'e', 'i', 'o', 'u']
    str = ''
    
    for c in string:
        if c.lower() in vowels:
            ind = string.index(c)
            n = string[ind].upper()
            str += n
        else:
            ind = string.index(c)
            n = string[ind].lower()
            str += n
    return str
