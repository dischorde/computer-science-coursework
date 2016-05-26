# Problem 4
# Write a Python function that returns True if aString is a palindrome (reads the same forwards or reversed) and False otherwise. Do not use Python's built-in reverse function or aString[::-1] to reverse strings
def isPalindrome(aString):
    """
    Iterative isPalindrome because I'm angry with my recursive version not working
    """
    if aString == '':
        return True
    beg = 0
    end = len(aString) - 1
    while end >= beg:
        if beg + 1 == end:
            if aString[beg] == aString[end]:
                return True
            else:
                return False
        elif beg == end:
            return True
        elif aString[beg] != aString[end]:
            return False
        else:
            beg += 1
            end -= 1

def isTrue(aString):
    if aString == 'goddog':
        return True
    else:
        return False
    return False
    
# Problem 5
# Write a Python function that returns the sum of the pairwise products of listA and listB. You should assume that listA and listB have the same length and are two lists of integer numbers. For example, if listA = [1, 2, 3] and listB = [4, 5, 6], the dot product is 1*4 + 2*5 + 3*6, meaning your function should return: 32
# Hint: You will need to traverse both lists in parallel.
# This function takes in two lists of numbers and returns a number.

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    Alist = listA[:]
    Blist = listB[:]
    ans = 0
    while len(Alist) != 0:
        ans += Alist[0] * Blist[0]
        Alist.pop(0)
        Blist.pop(0)
    return ans

# Problem 6
# Write a function to flatten a list. The list contains other lists, strings, or ints. For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into [1,'a','cat',2,3,'dog',4,5]
def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    flattened = []
    for item in aList:
        if type(item) == list:
            flattened.extend(flatten(item))
        else:
            flattened.append(item)
    return flattened

# Problem 7
# Write a function called dict_interdiff that takes in two dictionaries (d1 and d2). The function will return a tuple of two dictionaries: a dictionary of the intersect of d1 and d2 and a dictionary of the difference of d1 and d2
# intersect: The keys to the intersect dictionary are keys that are common in both d1 and d2. To get the values of the intersect dictionary, look at the common keys in d1 and d2 and apply the function f to these keys' values -- the value of the common key in d1 is the first parameter to the function and the value of the common key in d2 is the second parameter to the function. Do not implement f inside your dict_interdiff code -- assume it is defined outside.
# difference: a key-value pair in the difference dictionary is (a) every key-value pair in d1 whose key appears only in d1 and not in d2 or (b) every key-value pair in d2 whose key appears only in d2 and not in d1.

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    intersect = {}
    difference = {}
    dict1 = d1.copy()
    dict2 = d2.copy()
   
    for key in dict1.keys():
        if key not in dict2.keys():
            difference[key] = dict1[key]
        else:
            intersect[key] = f(dict1[key], dict2[key])
            del dict2[key]
    
    for key in dict2.keys():
        difference[key] = dict2[key]
    
    return (intersect, difference) 

# Problem 8
# Write a Python function called satisfiesF that has the specification below. Then make the function call run_satisfiesF(L, satisfiesF).
# After you define your function, make a function call to run_satisfiesF(L, satisfiesF). Do not define f or run_satisfiesF. Do not leave any debugging print statements.
# For this question, you will not be able to see the test cases we run. This problem will test your ability to come up with your own test cases.

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    iL = L[:]
    for s in iL:
        if f(s) == False:
            L.remove(s)
    return len(L)   

run_satisfiesF(L, satisfiesF)

