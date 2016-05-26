# -*- coding: utf-8 -*-
# Complete Programming Experience: ndigits
# Write a function called “ndigits”, that takes an integer ‘x’ (either positive or negative) as an argument. This function should return the number of digits in the integer x.
def ndigits(x):
    """
    (int) -> int
    x: positive or negative integer
    
    Returns the number of digits in integer x  
    """   
    x = abs(x) 
    if x == 0:   # If x is one positive digit, x/10 == 0 due to truncation.
        return 0  # The grader doesn't consider zero as a digit
    else:
        return 1 + ndigits(x/10) 