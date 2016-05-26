# Complete Programming Experience: polysum
# Write a function called 'polysum' that takes 2 arguments, 'n' and 's'. This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.
def polysum(n, s):
    """
    n: number of sides of a regular polygon
    s: length of each side
    
    Returns the sum of the area and square of the perimeter of a 
    regular polygon, rounded to 4 decimal places.
    
    The area of a regular polygon is .25*n*s^2/tan(pi/n)  
    """
    from math import pi, tan
    area = (.25 * n * (s**2)) / (tan(pi/n))
    perimeter = n * s
    return round(area + perimeter**2, 4)