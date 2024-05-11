"""
-------------------------------------------------------
Assignment 2, Task 5
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2023-09-30"
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
    
length = float(input("Foundation length (m): "))
width = float(input("Foundation width (m): "))
foun_height = float(input("Foundation height (m): "))
wall_height = float(input("Wall height (m): "))
cost_conc = float(input("Cost of concrete ($/m^3): "))
cost_brick = float(input("Cost of bricks ($/m^2): "))

area_conc = length * width * foun_height
total_conc = area_conc * cost_conc

area_brick = 2*wall_height*width + 2*wall_height*length
total_brick = area_brick * cost_brick

total_cost = total_conc + total_brick

print(f"Concrete needed for foundation (m^3): {area_conc:,.2f}")
print(f"Cost of concrete: $ {total_conc:,.2f}")
print(f"Bricks needed for walls (m^2): {area_brick:,.2f}")
print(f"Cost of bricks: $ {total_brick:,.2f}")
print(f"Total cost: $ {total_cost:,.2f}")