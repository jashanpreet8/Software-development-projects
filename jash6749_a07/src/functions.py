"""
-------------------------------------------------------
Assignment 7, Functions
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2023-11-17"
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

def list_factors(number):
    """
    -------------------------------------------------------
    takes an integer greater than 0 as a parameter (number) 
    and returns a list of the factors that make up that 
    number excepting the number itself
    Use: factors = list_factors(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 0)
    Returns:
        factors - list of factors of input (list)
    ------------------------------------------------------
    """
    list = []
    for i in range(1, number):
        if number % i == 0:
            list.append(i)
    return list
    
def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: number_list = list_positives()
    -------------------------------------------------------
    Returns:
        number_list - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    list = []
    num = int(input('Enter a positive number: '))
    while num != 0:
        if num > 0:
            list.append(num)
        num = int(input('Enter a positive number: '))
    return list
    
def get_indexes(numbers, target_number):
    """
    -------------------------------------------------------
    Finds the indexes of target_number in numbers.
    Use: index_list = get_indexes(numbers, target_number)
    -------------------------------------------------------
    Parameters:
        numbers - list of values (list)
        target_number - value to look for in num_list (*)
    Returns:
        index_list - list of indexes of target_number (list of int)
    -------------------------------------------------------
    """
    list = []
    length = len(numbers)
    for ind in range(length):
        if numbers[ind] == target_number:
            list.append(ind)
    return list
    
def list_subtract(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtract(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """
    for s in subtrahend:
        var = 0
        if s in minuend:
            inds = get_indexes(minuend, s)
            minuend.pop(inds[0])
            for i in inds[1:]:
                i = i - 1 - var
                var += 1
                minuend.pop(i)
    return None
    
def verify_sorted(numbers):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = verify_sorted(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers (list)
    Returns:
        in_order - True if numbers is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    """ 
    if numbers[0] > numbers[-1]:    
        list2 = []
        list2.append(numbers[0])
        for num in numbers[1:]:
            if num < list2[-1]:
                list2.append(num)
                in_order = True
                index = -1
            else:
                in_order = False
                index = numbers.index(num)-1
                break
    """
    list = []
    list.append(numbers[0])
    for num in numbers[1:]:
        if num > list[-1]:
            list.append(num)
            in_order = True
            index = -1
        else:
            in_order = False
            index = numbers.index(num)
            break
    
    return in_order, index