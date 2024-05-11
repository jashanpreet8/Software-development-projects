"""
-------------------------------------------------------
Midterm B Task 3 Function Definitions
-------------------------------------------------------
Author: Jashanpreet Singh Jashanpreet Singh
ID:     169046749
Email:  jash6749@mylaurier.ca
__updated__ = "2023-10-29"
-------------------------------------------------------
"""
# Constants
BASE = 125
EXTRA = 25
DISCOUNT = 0.10
# your constants here


def servicing():
    """
    -------------------------------------------------------
    Determines the cost of getting a home furnace tune up. The cost is made up of:
        base cost: $125.00
        cost per extra service: $25.00
        VIP discount 10% only if:
            more than 1 extra service purchased
            and purchaser is a VIP
    The function must ask the user for these inputs.
    Use: cost = servicing()
    -------------------------------------------------------
    Returns‌​‌​​​​‌​​‌‌​‌‌‌​​‌​‌‌​‌‌‌​‌:
        cost - cost of getting a home furnace tune up based upon the base cost,
            the number of extra services purchased, and VIP discount
            if applicable (float)
    -------------------------------------------------------
    """

    # your code here
    add = int(input('How many extra services are you purchasing? '))
    if add > 1:
        vip = input('Are you a VIP member (Y/N)? ')
        if vip == 'Y':
            cost = (BASE + EXTRA*add) - DISCOUNT*(BASE + EXTRA*add)
        elif vip == 'N':
            cost = (BASE + EXTRA*add)
    else:
        cost = (BASE + EXTRA*add)
    
    return cost
