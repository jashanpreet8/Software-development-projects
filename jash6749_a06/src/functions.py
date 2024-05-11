"""
-------------------------------------------------------
Assignment 6, Functions
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2023-11-08"
-------------------------------------------------------
"""
# Imports
from ast import Num

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
    
def total_wins():
    """
    -------------------------------------------------------
    asks the user to enter a series of strings that represent
    the output of a game with a loop
    Use: num1, num2 = total_wins()
    -------------------------------------------------------
    Parameters:
        None
    Returns:
        num1, num2 - represent the highest number of times
        two strings are entered (int)
    ------------------------------------------------------
    """
    purple, gold = 0, 0
    inp = input("Enter the winning team: ")
    while inp != '':
        if inp == 'purple':
            purple += 1
        elif inp == 'gold':
            gold += 1
        inp = input("Enter the winning team: ")
    return purple, gold
    
def detect_prime(number):
    """
    -------------------------------------------------------
    Determines if number is a prime number.
    Use: prime = detect_prime(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        prime - True if number is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    num = number - 1
    prime = True
    if number == 2:
        prime = False
    while num > 1:
        if number % num == 0:
            prime = False
        num -= 1
    return prime
    
def interest_table(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest interest_rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    print(f'Principal: ${principal_amount}')
    print(f'Interest Rate: {interest_rate}%')
    print(f'Monthly Payment: ${payment}')
    print('----------------------------------')
    print('Month Interest   Payment   Balance')
    print('----------------------------------')
    
    month = 1
    balance = principal_amount
    while balance>0:
        int = (interest_rate/12/100)*balance
        if payment > balance:
            payment = balance + int
        balance = balance-payment+int
        print(f"{month:5d}{int:>9.2f}{payment:>10.2f}{balance:>10.2f}")
        month += 1
    return None
    
def count_of_digits(number):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: digits = count_of_digits(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        digits - the number of digits in number (int)
    ------------------------------------------------------
    """
    if number < 0:
        number *= -1
    count = 1
    mul = 10
    while number // mul > 0:
        count += 1
        mul *= 10 
    return count
    
    
def factor_summation(number):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = factor_summation(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        total - the total of number's factors (int)
    ------------------------------------------------------
    """
    total = 0
    num = number-1
    while num > 0:
        if number % num == 0:
            total += num
        num -= 1
    return total