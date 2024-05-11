"""
-------------------------------------------------------
Assignment 5, Functions
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2023-10-30"
-------------------------------------------------------
"""
# Imports

# Constants

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
    
def calc_factorial(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = calc_factorial(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """
    product = 1
    for i in range(1, number+1, 1):
        product *= i
    return product
    
def calories_treadmill(per_min, minutes):
    """
    -------------------------------------------------------
    Calculates the number of calories burned every five
    minutes given the number of calories burned per minute 
    (per_min) an the total number of minutes run (minutes).
    Use: calories_treadmill(per_min, minutes)
    -------------------------------------------------------
    Parameters:
        per_min - number of calories burned per minute (float)
        minutes - total number of minutes run (float)
    Returns:
        None
    ------------------------------------------------------
    """
    print_min = 0
    for i in range(5, minutes+1, 5):
        if minutes >= 5:
            print_min += 5
            minutes -= 5
        elif minutes < 5:
            print_min = minutes
        
        calories = print_min*per_min
        print(f"{print_min:2d}  {calories:>5.1f}")
        
    return None   
    
def arrow_up(rows):
    """
    -------------------------------------------------------
    Prints a arrow of # characters pointing up.
    Use: arrow_up(rows)
    -------------------------------------------------------
    Parameters:
        rows - the number of rows for the arrow (int)
    Returns:
        None
    ------------------------------------------------------
    """
    inner_space = 0
    for i in range(rows, 0, -1):
        print(" "*(i-1), end="")
        print("#", end="")
        if inner_space <= 1: 
            print(" "*inner_space, end="")
        else:
            print(" "*(2*inner_space-1), end="")
        if inner_space == 0:
            print()
        else:
            print("#")
        inner_space += 1
    
    
def multiplication_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: multiplication_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    count_num = 0
    print("   ", end="")
    for i in range(start_num, stop_num+1):
        print(f"{i:5d}", end="")
        count_num += 1
    print()
    print(f"   {('-----'*count_num)}")
    for i in range(start_num, stop_num+1):
        print(f"{i} |", end="")
        for j in range(start_num, stop_num+1):
            print(f"{(i*j):5d}", end="")
        print()
    return None
    
    
def range_addition(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum values from start by increment.
    Use: total = range_addition(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    total = 0
    for i in range(start, increment*count, increment):
        total += i
    return total
        