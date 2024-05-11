"""
-------------------------------------------------------
Exam Task 1 Function Definitions
-------------------------------------------------------
Author: Jashanpreet Singh Jashanpreet Singh
ID:     169046749
Email:  jash6749@mylaurier.ca
__updated__ = "2023-08-25"
-------------------------------------------------------
"""


def even_avg(values):
    """
    -------------------------------------------------------
    Returns the average (integer, rounded down) of all even numbers
    in values. If values has no even numbers, the average is 0.
    Use: ea = even_avg(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of int)
    Returns‌​‌​​​​‌​​‌‌​‌‌‌​​‌​‌‌​‌‌‌​‌:
        ea - the average of the even numbers in values (int)
    -------------------------------------------------------
    """

    # your code here
    total = 0
    count = 0
    for value in values:
        if value%2 == 0:
            total += value
            count += 1
    
    if total == 0:
        avg = 0
    else:
        avg = total/count
    return int(avg)
