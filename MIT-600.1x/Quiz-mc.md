Problem 1**strong text**

1) Suppose x = "pi" and y = "pie". The line of code x, y = y, x will swap the values of x and y, resulting in x = "pie" and y = "pi".

 True - correct 

2) Suppose x is an integer in the following code:
<code> def f(x):
    while x > 3:
        f(x+1) </code>

For any value of x, all calls to f are guaranteed to never terminate.

False - correct

3) A Python program always executes every line of code written at least once.

False - correct

4) Suppose you have two different functions that each assign a variable called x. Modifying x in one function means you always modify x in the other function for any x.

False - correct

5) The following code will enter an infinite loop for all values of i and j.

<code> while i >= 0:
    while j >= 0:
        print i, j </code>
        
False - correct

7) Assume f() is defined. In the statement a = f(), a is always a function.

False - correct

8) A program that keeps running and does not stop is an example of a syntax error.

False - correct

9) Consider the following function.
<code> def f(x):
    a = []
    while x > 0:
        a.append(x)
        f(x-1) </code>

A new object of type list is created for each recursive invocation of f.

True - correct 

10) A tuple can contain a list as an element.

True  - correct 

**Problem 2-1**
Consider the statement: L = {'1':1, '2':2, '3':3}. Which is correct?

L maps strings to integers - correct

**Problem 2-2**
Assume a break statement is executed inside a loop and that the loop is inside a function. Which of the following is correct?

 The loop will always immediately terminate. The loop will always immediately terminate. - incorrect  
 
**Problem 2-3**
In Python, which of the following is a mutable object?

 a list - correct  
 
**Problem 2-4**

Assume the statement s[1024] = 3 does not produce an error message. This implies:

 type(s) can be str  
 type(s) can be list 
 All of the above - incorrect

**Problem 2-5**
Consider the code:

<code> L = [1,2,3]
d = {'a': 'b'}
def f(x):
    return 3 </code>
    
Which of the following does NOT cause an exception to be thrown?

<code> print L[3] </code> 
<code> print d['b'] </code>
<code> for i in range(1000001, -1, -2):
    print f </code>
None of the above - incorrect

**Problem 3-1**

Examine the following code snippet:

  <code> stuff  = _____
  for thing in stuff:
        if thing == 'iQ':
           print "Found it" </code>
           
Select all the values of the variable "stuff" that will make the code print "Found it".

["iBoy", "iGirl", "iQ", "iC","iPaid","iPad"]
, ("iBoy", "iGirl", "iQ", "iC","iPaid","iPad"), 
["iQ"], - This answer is correct.

**Problem 3-2**

The following Python code is supposed to compute the square of an integer by using successive additions.

<code> def Square(x):
    return SquareHelper(abs(x), abs(x)) </code>

<code> def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x </code>
    
Not considering recursion depth limitations, what is wrong with this implementation of procedure Square? Check all that apply.

Nothing is wrong; the code is fine as-is. , - This answer is correct.
