**Problem 1**

1) In the statement <code> L = [1,2,3], L </code> is a class.

False - correct

2) The orders of growth of O(n^2+1) and O(n^5+1) are both polynomial.

True - correct

3) The complexity of binary search on a sorted list of n items is O(log⁡n).

 True - correct 
 
4) A bisection search algorithm always returns the correct answer when searching for an element in a sorted list.

 True - correct
 
5) Performing binary search on an unsorted list will always return the correct answer in O(n) time where n is the length of the list.

False - correct

**Problem 2-1**
You have the following class hierarchy:

<code> class A(object):
    def foo(self):
        print 'hi'
class B(A):
    def foo(self):
        print 'bye' </code>
          
Which of the following is correct?
When a = A() we say that a is an instance of A  
When b = B() we say that b is a subclass of A  
Both of the above  - incorrect 
// Is not b an instance of a subclass of A?? I felt this was a trick question. b is obviously not a subclass itself because it is an object, but if that object is an instance of a subclass was that answer false (as was the obvious answer) or true due to that technicality? Apparently the obvious... this time. - . -

**Problem 2-2**
Consider the function f below. What is its Big O complexity?

<code>
def f(n):
    def g(m):
        m = 0
        for i in range(m):
            print m
    for i in range(n):
        g(n)
        </code>

O(n^2) - incorrect
//  And I got tricked again. Why in the world would you set m = 0 in g(m) and therefore throw out whatever you pass in? Here I was assuming I was overthinking since I just missed problem 2-1 due to that and didn't scour the details for anything illogical specifically there to trick...

**Problem 2-3**
A dictionary is an immutable object because its keys are immutable.

 False because a dictionary is mutable - correct

**Problem 2-4**

Consider the following two functions and select the correct choice below:

<code> def foo_one(n):
    """ Assume n is an int >= 0 """
    answer = 1.0
    while n > 1:
        answer *= n
        n -= 1
    return answer </code>

<code> def foo_two(n):
    """ Assume n is an int >= 0 """
    if n <= 1: 
        return 1.0
    else: 
        return n*foo_two(n-1) </code>

The worst case Big Oh time complexity of <code>foo_one</code> and <code>foo_two</code> are the same. - correct

**Problem 2-5**

The complexity of 1^n+n^4+4n+4 is

exponential - incorrect

// Obviously this is polynomial when you remember your basic math skills that 1^anything is 1. In effect, this was a corner case for my mental algorithm for determining big O, which I think is kind of cruel as the question is testing more "common sense" (did you catch that the constant was 1?) than what we were specifically taught (constant raised to a power -> exponential big O).