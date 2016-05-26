# Complete Programming Experience: Python Loves Fruits 

# Python is an MIT student who loves fruits. He carries different types of 
# fruits (represented by capital letters) daily from his house to the MIT campus 
# to eat on the way. But the way he eats fruits is unique. After each fruit he 
# eats (except the last one which he eats just on reaching the campus), he takes a
# 30 second break in which he buys 1 fruit of each type other than the one he just
# had. Cobra, his close friend, one day decided to keep a check on Python. He 
# followed him on his way to MIT campus and noted down the type of fruit he ate in
# the form of a string pattern (Eg.: 'AABBBBCA'). Can you help Cobra determine the
# maximum quantity out of the different types of fruits that is present with 
# Python when he has reached the campus?


def nfruits(basket, pattern):
    """
    (dictionary, string) -> int
    
    Returns the max quantity of fruits of a single type Python has when he reaches MIT.
    For MIT 6.00.1x Spring 2016, "Python Loves Fruits" Exercise. 
    
    basket: A non-empty dictionary containing a letter representing a type of fruit
    and its quantity initially with Python when he leaves home (length < 10)
    
    pattern: A string pattern of letters representing the fruits eaten by Python on his journey
    """   
    carrying = basket.copy()
    fruitsleft = len(pattern) #fruits remaining to eat
    for letter in pattern:
        carrying[letter] -= 1
        fruitsleft -= 1
        # if fruits still remaining, meaning not at MIT
        if fruitsleft > 0:
            for fruit in carrying.keys(): 
                #buy more of everything else
                if letter != fruit:   
                    carrying[fruit] += 1 
    
    return max(carrying.values())
