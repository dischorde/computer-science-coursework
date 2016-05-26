# Problem 1-1: Counting Vowels
# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s

s = raw_input('String to test: ')
count = 0
for char in s:
    if char.lower() in 'aeiou':   
        count += 1
print 'Number of vowels: ',
print str(count)

# Problem 1-2: Counting Bobs
# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s. 

count = 0
n = len(s)
for i in range(n-2):
    if s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b':
        count += 1
print 'Number of times bob occurs is: ',
print str(count)

# Problem 1-2: Counting Bobs Alternate Version
# This will count only non-overlapping bobs

s = raw_input('String to test: ')
count = s.count('bob')
print 'Number of times bob occurs is: ',
print str(count)


# Problem 1-3:  Counting and Grouping
# Write a function called item_order that takes as input a string named order. 
# The string contains only words for the items the customer can order separated by one space. 
# The function returns a string that counts the number of each item and consolidates them in the following order: salad:[# salad] hamburger:[# hambruger] water:[# water]

def item_order(order):
    '''
    order: a string contains only words for the items the customer can order 
    separated by one space. The items that a customer can order are: salad, 
    hamburger, and water.

    returns:a string that counts the number of each item and consolidates them 
    in the following order: salad:[# salad] hamburger:[# hambruger] water:[# water
    '''
    salad = order.count('salad')   #unlike pset 1.2, we need non-overlapping #s
    burger = order.count('hamburger')
    water = order.count('water')
    return 'salad:' + str(salad) + ' hamburger:' + str(burger) + ' water:' + str(water)