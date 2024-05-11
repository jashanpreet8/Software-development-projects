"""
-------------------------------------------------------
Midterm B Task 2 Function Definitions
-------------------------------------------------------
Author: Jashanpreet Singh Jashanpreet Singh
ID:     169046749
Email:  jash6749@mylaurier.ca
__updated__ = "2023-10-31"
-------------------------------------------------------
"""


def categorize(strokes):
    """
    -------------------------------------------------------
    Determines the golf skill rating given number of strokes to complete 18 holes.
        If strokes are 70 or less, the rating is "Grandmaster".
        If strokes are 85 or less, the rating is "Master".
        If strokes are 100 or less, the rating is "Professional".
        If strokes are greater than 100, the rating is "Amateur".
        If points is less than 0, return "Error"
    Must use a fallthrough algorithm.
    Use: rating = categorize(strokes)
    -------------------------------------------------------
    Parameters:
        strokes - strokes to complete 18 holes of golf (int >= 0)
    Returns‌​‌​​​​‌​​‌‌​‌‌‌​​‌​‌‌​‌‌‌​‌:
        category - description of skill rating (str)
    -------------------------------------------------------
    """

    if 0 <= strokes <= 70:
        category = 'Grandmaster'
    elif 70 < strokes <= 85:
        category = 'Master'
    elif 85 < strokes <= 100:
        category = 'Professional'
    elif strokes > 100:
        category = 'Amateur'
    else:
        category = 'Error'
        

    return category
