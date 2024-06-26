"""
-------------------------------------------------------
Exam Task 2 Function Definitions
-------------------------------------------------------
Author: Jashanpreet Singh Jashanpreet Singh
ID:     169046749
Email:  jash6749@mylaurier.ca
__updated__ = "2023-08-25"
-------------------------------------------------------
"""
# Constants

# Your constants here
DRY = 4
DAMP = 8
SENTINEL = -1

def rainfall():
    """
    -------------------------------------------------------
    Asks the user for daily rainfall (in mm) from the keyboard.
    The function stops asking for rainfall when the user enters -1.
    The function returns:
        the total number of dry days (rainfall lower than 4mm)
        the total number of damp days (rainfall 4mm - 8mm)
        the total number of wet days (rainfall greater than 8mm)
        the average rainfall for all days (rounded down)
    Do all inputs and calculations in integer.
    Use: dry_days, damp_days, wet_days, avg = rainfall()
    -------------------------------------------------------
    Returns‌​‌​​​​‌​​‌‌​‌‌‌​​‌​‌‌​‌‌‌​‌:
        dry_days - number of dry days (int)
        damp_days - number of damp days (int)
        wet_days - number of wet days (int)
        avg - average rainfall of all days (int)
    -------------------------------------------------------
    """

    # your code here
    dry, damp, wet, total, count = 0, 0, 0, 0, 0
    
    rain = int(input('Rainfall mm (-1 to stop): '))
    while rain != SENTINEL:
        total += rain
        count += 1
        if rain < DRY:
            dry += 1
        elif DRY <= rain <= DAMP:
            damp += 1
        elif rain > DAMP:
            wet += 1
        rain = int(input('Rainfall mm (-1 to stop): '))    
    
    avg = int(total/count)    

    return dry, damp, wet, avg
