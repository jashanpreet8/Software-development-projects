"""
-------------------------------------------------------
Lab 5 Functions
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2023-10-18"
-------------------------------------------------------
"""
# Imports

# Constants
ACC = 9.8
INFANT = 3
SENIOR = 65
ADULT = 18
KID = 10

def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """
    
def get_weight(mass):
    """
    -------------------------------------------------------
    Describes a mass in terms of its weight. If its weight is > 1000 N,
    it is "heavy", less than 10 N it is "light", and "average" otherwise.
    weight = mass (kg)  acceleration due to gravity (9.8/m/s^2)
    Use: weight, message = get_weight(mass)
    -------------------------------------------------------
    Parameters:
        mass - mass of an object in kg (float > 0)
    Returns:
        weight - weight of an object in Newtons (float)
        message - description of weight of object (str)
    -------------------------------------------------------
    """
    weight = mass * ACC
    if weight < 10:
        msg = "light"
    elif weight > 1000:
        msg = "heavy"
    else:
        msg = "average"
    return weight, msg

def is_leap(year):
    """
    -------------------------------------------------------
    Determines if a year is a leap year. Every year that is
    exactly divisible by four is a leap year, except for years
    that are exactly divisible by 100, but these centurial years
    are leap years if they are exactly divisible by 400. For
    example, the years 1700, 1800, and 1900 are not leap years,
    but the years 1600 and 2000 are.
    Use: result = is_leap(year)
    -------------------------------------------------------
    Parameters:
        year - a year (int > 0)
    Returns:
        result - True if year is a leap year,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                result = True
            else:
                result = False
        else:
            result = True
    else:
        result = False
    return result

def wind_speed(speed):
    """
    -------------------------------------------------------
    description
    Use: category = wind_speed(speed)
    -------------------------------------------------------
    Parameters:
        speed - wind speed in km/hr (int >= 0)
    Returns:
        category - description of wind speed (str)
    ------------------------------------------------------
    """
    if speed >= 0:
        if speed < 39:
            ctg = 'Breeze'
        elif 39 <= speed <= 61:
            ctg = 'Strong Wind'
        elif 62 <= speed <= 88:
            ctg = 'Gale Winds'
        elif 89 <= speed <= 117:
            ctg = 'Whole Gale'
        elif speed > 117:
            ctg = 'Hurricane'
    else:
        ctg = 'Unknown'
    return ctg

def quadrant(x, y):
    """
    -------------------------------------------------------
    Determines location on a plane of an x, y coordinate.
    Use: location = quadrant(x, y)
    -------------------------------------------------------
    Parameters:
        x - x coordinate on a Cartesian plane (float)
        y - y coordinate on a Cartesian plane (float)
    Returns:
        location - one of: 'Quadrant 1', 'Quadrant 2', 'Quadrant 3'
          'Quadrant 4', 'X-Axis', 'Y-Axis', 'Origin' (str)
    -------------------------------------------------------
    """
    if x > 0:
        if y > 0:
            quad = 'Quadrant 1'
        elif y < 0:
            quad = 'Quadrant 4'
        else:
            quad = 'X-Axis'
    elif x < 0:
        if y > 0:
            quad = 'Quadrant 2'
        elif y < 0:
            quad = 'Quadrant 3'
        else:
            quad = 'X-Axis'
    else:
        if y != 0:
            quad = 'Y-Axis'
        else:
            quad = 'Origin'
    return quad

def ticket():
    """
    -------------------------------------------------------
    School play ticket price calculation.
    Asks user for their age, and if necessary, if they are
    a student at the school. Prices:
        Infant (age < 3): $0
        Senior (age >= 65): $4.00
        Student (10 <= age < 18): $3.00
            Student of this school: $1.00
        Adult (18 <= age < 65): $5.00
        Kid (3 <= age < 10): $2.00
    Use: price = ticket()
    -------------------------------------------------------
    Returns:
        price - the price of one ticket (float)
    -------------------------------------------------------
    """
    age = float(input('How old are you? '))
    if age < INFANT:
        price = 0
    elif age >= SENIOR:
        price = 4
    elif KID <= age < ADULT:
        student = input('Are you a student at this school(Y/N)? ')
        if student == 'Y' or student =='y':
            price = 1
        elif student == 'N' or student == 'n':
            price = 3
    elif ADULT <= age < SENIOR:
        price = 5
    elif INFANT <= age < KID:
        price = 2
    return price