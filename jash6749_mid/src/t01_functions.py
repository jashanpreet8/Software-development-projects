"""
-------------------------------------------------------
Midterm B Task 1 Function Definitions
-------------------------------------------------------
Author: Jashanpreet Singh Jashanpreet Singh
ID:     169046749
Email:  jash6749@mylaurier.ca
__updated__ = "2023-10-29"
-------------------------------------------------------
"""
# Constants
LOONIES = 100
QUARTERS = 25
DIMES = 10
NICKELS = 5


def minimal_change(cents):
    """
    -------------------------------------------------------
    Breaks down cents into a minimal number of coins.
    The change can be:
        loonies - coins worth 100 cents
        quarters - coins worth 25 cents
        dimes - coins worth 10 cents
        nickels - coins worth 5 cents
    Use: loonies, quarters, dimes, nickels = minimal_change(cents)
    -------------------------------------------------------
    Parameters:
        cents - number of cents (int >= 0)
    Returns‌​‌​​​​‌​​‌‌​‌‌‌​​‌​‌‌​‌‌‌​‌:
        loonies - number of loonies ($1 coins) (int)
        quarters - number of quarters (25 cent coins) (int)
        dimes - number of dimes (10 cent coins) (int)
        nickels - number of nickels (5 cent coins) (int)
    -------------------------------------------------------
    """

    # your code here
    loonies, quarters, dimes, nickels = 0, 0, 0, 0
    if cents // LOONIES != 0:
        loonies = cents // LOONIES
    cent_left = cents % LOONIES
    if cent_left // QUARTERS != 0:
        quarters = cent_left // QUARTERS
    cent_left = cent_left  % QUARTERS
    if cent_left // DIMES != 0:
        dimes = cent_left // DIMES
    cent_left = cent_left % DIMES
    if cent_left // NICKELS != 0:
        nickels = cent_left // NICKELS
    cent_left = cent_left % NICKELS
        

    return loonies, quarters, dimes, nickels
