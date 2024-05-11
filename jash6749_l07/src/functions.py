"""
-------------------------------------------------------
Lab 7, Functions
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2023-10-30"
-------------------------------------------------------
"""
# Imports
from random import randint
from math import inf
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

def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    number = randint(1, high)
    guess = 0
    count = 0
    while guess != number:
        guess = int(input('Guess: '))
        count += 1
        if guess > number:
            print('Too high, try again')
        elif guess < number:
            print('Too low, try again')
        else:
            print('Congratulations - good guess!')
    return count

def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """
    power = 1
    n = 0
    while power < target:
        power = 2**n
        n += 1
    return power
    
def positive_statistics():
    """
    -------------------------------------------------------
    Asks a user to enter a series of positive numbers, then calculates
    and returns the minimum, maximum, total, and average of those numbers.
    Stop processing values when the user enters a negative number.
    The first number entered must be positive.
    Use: minimum, maximum, total, average = positive_statistics()
    -------------------------------------------------------
    Returns:
        minimum - smallest of the entered values (float)
        maximum - largest of the entered values (float)
        total - total of the entered values (float)
        average - average of the entered values (float)
    ------------------------------------------------------
    """
    first = float(input('First positive value: '))
    nxt = first
    count = 1
    total = first
    mini = first
    maxi = first
    
    while nxt >= 0:
        nxt = float(input('Next positive value: '))
        if nxt >= 0:
            count += 1
            total += nxt
            if mini > nxt and nxt >= 0:
                mini = nxt
            if maxi < nxt:
                maxi = nxt
        
    average = total/count
    return mini, maxi, total, average
    
def budget(available):
    """
    -------------------------------------------------------
    Asks a user for a series of expenses in a month. Calculate the
    total expenses and determines whether the user is in "Surplus",
    "Deficit", or "Balanced" status.
    Use: expenses, balance, status = budget(available)
    -------------------------------------------------------
    Parameters:
        available - money currently available (float >= 0)
    Returns:
        expenses - total monthly expenses (float)
        balance - remaining balance (float)
        status - One of (str):
            "Surplus" if user budget is in surplus
            "Deficit" if user budget is in deficit
            "Balanced" if user budget is balanced
    ------------------------------------------------------
    """
    exp1 = float(input('Enter an expense (0 to quit): $'))
    exp2 = exp1
    expenses = exp1
    
    while exp2 > 0:
        exp2 = float(input('Enter another expense (0 to quit): $'))
        expenses += exp2
    
    balance = available-expenses
    if balance > available:
        status = 'Surplus'
    elif balance < available:
        status = 'Deficit'
    else:
        status = 'Balanced'
        
    return expenses, balance, status
    

def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    -------------------------------------------------------
    """
    id = float(input('Employee ID: '))
    total = 0
    count = 0
    
    while id > 0:
        wage = float(input('Hourly wage rate: '))
        hours = float(input('Hours worked: '))
        
        OVERTIME = hours-40
        OVERTIME_RATE = wage*1.5
        TAX_RATE = 3.625/100
        
        if hours > 40:
            bt = 40*wage + (hours-40)*wage*1.5
        else:
            bt = hours*wage
            
        at = bt-(3.625*bt/100)
        
        print(f'Net payment for employee {id}: ${at:,.2f}')
        print()
        
        total += at        
        count += 1
        id = float(input('Employee ID: '))

    average = total/count
    return total, average