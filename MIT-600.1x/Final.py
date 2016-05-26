# Problem 3
# Write a function called dict_invert that takes in a dictionary with immutable values and returns the inverse of the dictionary. The inverse of a dictionary d is another dictionary whose keys are the unique dictionary values in d. The value for a key in the inverse dictionary is a sorted list of all keys in d that have the same value in d.
def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    d_invert = {}
    for key in d.keys():
        try:
            d_invert[d[key]].append(key)
            d_invert[d[key]].sort()
        except KeyError:
            d_invert[d[key]] = [key]
    return d_invert

# Problem 4 - Part 1
# Write a function called getSublists, which takes as parameters a list of integers named L and an integer named n. assume L is not empty. assume 0 < n <= len(L)
# This function returns a list of all possible sublists in L of length n without skipping elements in L. The sublists in the returned list should be ordered in the way they appear in L, with those sublists starting from a smaller index being at the front of the list.
def getSublists(L, n):
    '''
    L: a list of integer 
    n: an integer
    
    Returns a list of all possible sublists in L of length n
    without skipping elements in L. Assumes L is not empty & 0 < n <= len(L)
    '''
    master = []
    for i in range(len(L)):
        if (i + n) > len(L):
            break
        else:
            sub = []
            for j in range(i,i+n):
                sub.append(L[j])
            master.append(sub)
    return master

# Problem 4 - Part 2
# Write a function called longestRun, which takes as a parameter a list of integers named L (assume L is not empty). This function returns the length of the longest run of monotonically increasing numbers occurring in L. A run of monotonically increasing numbers means that a number at position k+1 in the sequence is either greater than or equal to the number at position k in the sequence.
def longestRun(L):    
    '''
    L: a list of integers (assume L is not empty). 

    This function returns the length of the longest run of monotonically increasing
    numbers occurring in L. A run of monotonically increasing numbers means that a
    number at position k+1 in the sequence is either greater than or equal to the 
    number at position k in the sequence.
    '''      
    runs = []    
    length = 1
    
    for k in range(len(L) - 1):
        if L[k] <= L[k+1]:
            length += 1
            if k == len(L) - 2:
                runs.append(length)
        else:
            runs.append(length)
            length = 1 
              
    try:
        return max(runs)
    except:
        return 1

# Problem 5
# In this problem, you will implement a class according to the specifications in the template file usresident.py. The file contains a Person class similar to what you have seen in lecture and a USResident class (a subclass of Person). Person is already implemented for you and you will have to implement two methods of USResident.
## DO NOT MODIFY THE IMPLEMENTATION OF THE Person CLASS ##
class Person(object):
    def __init__(self, name):
        #create a person with name name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name
        self.age = None
    def getLastName(self):
        #return self's last name
        return self.lastName
    def setAge(self, age):
        #assumes age is an int greater than 0
        #sets self's age to age (in years)
        self.age = age
    def getAge(self):
        #assumes that self's age has been set
        #returns self's current age in years
        if self.age == None:
            raise ValueError
        return self.age
    def __lt__(self, other):
        #return True if self's name is lexicographically less
        #than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def __str__(self):
        #return self's name
        return self.name
        
class USResident(Person):
    """ 
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        Person.__init__(self, name)
        if status != 'citizen' and status != 'legal_resident' and status != 'illegal_resident':
            raise ValueError
        else:
            self.status = status
    def getStatus(self):
        return self.status

# Problem 6-1

class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return 'Prof. ' + self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def lecture(self, stuff): 
        return 'It is obvious that ' + Lecturer.lecture(self, stuff)
