"""
-------------------------------------------------------
Assignment 8, Functions
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2023-11-23"
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
    
def add_spaces(sentence):
    """
    -------------------------------------------------------
    Create a new sentence with added space between words. Words start
    with upper-case characters.
    Use: spaced = add_spaces(sentence)
    -------------------------------------------------------
    Parameters:
        sentence - sentence that represents a sentence in which all the
            words are run together (no spaces), but the first character
            of each word is uppercase. sentence has at least one
            character (str)
    Returns:
        spaced - new sentence in which the words are separated
            by spaces and only the first word starts with
            an uppercase character (str)
    -------------------------------------------------------
    """
    new = sentence[0]
    for c in sentence[1:]:
        if c.isupper():
            new += " "
            new += c.lower()
        else:
            new += c
    return new


def pluralize(string):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if string ends with 's', 'sh', or 'ch', add 'es'
        - if string ends with 'y' but not 'ay' or 'oy', replace
            the 'y' with 'ies'
        - otherwise add 's'
    Use: pluralized = pluralize(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        pluralized - a pluralized_string version of string (str)
    -------------------------------------------------------
    """
    plu = string
    if string[-1] == 's' or string[-2:] == 'sh' or string[-2:] == 'ch':
        plu += 'es'
    elif string[-1] == 'y' and string[-2:] != 'ay' and string[-2:] != 'oy':
        plu = plu[:-1]
        plu += 'ies'
    else:
        plu += 's'
    return plu

def common_end(str1, str2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: suffix = common_end(str1, str2)
    -------------------------------------------------------
    Parameters:
        str1 - first string for ending comparison (str)
        str2 - second string for ending comparison (str)
    Returns:
        suffix - the longest common ending of str1 and str2 (str)
    -------------------------------------------------------
    """ 
    suff = ''   
    ind = -1
    same = True
    
    while (same == True) and (suff != str1):
        if ind == -1:
            if str1[ind:] == str2[ind:]:
                ind -= 1
            else:
                same = False
        else:
            if str1[ind:ind+1] == str2[ind:ind+1]:
                ind -= 1
            else:
                same = False
        if -1*ind == len(str1):
            suff = str1
    
    if ind == -1:
        suff = ""
    elif ind != -1 and -1*ind != len(str1):    
        suff = str1[ind+1:]
    return suff
     
def valid_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: is_valid = valid_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        is_valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """
    groups = isbn.split('-')
    for group in groups:
        if group == '':
            empty = True
            break
        else:
            empty = False
    
    if isbn.replace('-', '').isdigit() and len(isbn) == 17 and len(groups) == 5 and empty != True and (groups[0] == '978' or groups[0] == '979') and groups[-1].isdigit() and len(groups[-1]) == 1:
        is_valid = True
    else:
        is_valid = False
    return is_valid
    
def has_word_chain(words):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: word_chain = has_word_chain(words)
    -------------------------------------------------------
    Parameters:
        words - a of strings (list of str, len > 1)
    Returns:
        word_chain - True if words is a word chain,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    ind = 1
    chain = True
    last = words[0][-1]
    
    while ind != len(words):
        first = words[ind][0:1]
        if last != first:
            chain = False
        last = words[ind][-1]
        ind += 1
        
    return chain
