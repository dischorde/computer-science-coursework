
# Problem Set 5

**Problem 1-1**
The ONLY thing we are interested in when designing programs is that it returns the correct answer.
    False - correct

**Problem 1-2**
Roughly speaking, under the RAM model of computation, adding two numbers takes the same amount of time as dividing them.
 True - correct 
 
**Problem 1-3**
When determining asymptotic complexity, we discard all terms except for the one with the largest growth rate.
True - correct  

**Problem 1-4**
Bisection search is an example of linear time complexity
False - correct

**Problem 1-5**

For large values of n, an algorithm that takes 20000n^2 steps has better time complexity (takes less time) than one that takes 0.001n^5 steps
True - correct

**Problem 2-1**
Indirection, as talked about in lecture, means you have to traverse the list more than once.
 False - correct
 
**Problem 2-2**
The complexity of binary search on a sorted list of n items is O(log⁡n).
True - correct  

**Problem 2-3**
The worst case time complexity for selection sort is O(n2).
True - correct
 
**Problem 2-4**
The base case for the recursive version of merge sort from lecture is checking ONLY for the list being empty.
False - correct

**Problem 2-5**
An ideal hash function maps all the input keys to the same output.
False - correct

**Problem 3**
For each of the following expressions, select the order of growth class that best describes it from the following list: <code>  O(1), O(log⁡(n)), O(n), O(nlog⁡(n)), O(nc) or O(cn). </code>  
Assume c is some constant.

<code>0.0000001n+1000000</code>  
O(n) - This answer is correct. 

<code>0.0001n^2+20000n−90000</code>  
O(n^c) - This answer is correct. 

<code>20n+900log⁡(n)+100000</code>  
O(n) - This answer is correct. 

<code>(log⁡(n))^2+5n^7</code>  
O(n^c) - This answer is correct. 

<code>n^200−2n^30</code>  
O(n^c) - This answer is correct. 

<code>30n^2+nlog⁡(n)</code>  
O(n^c) - This answer is correct. 

<code>nlog⁡(n)−3000n </code>  
O(n log(n)) - This answer is correct. 

<code>3</code>  
O(1) - This answer is correct. 

<code>5^n+n^5+n+5 </code>  
O(c^n) - This answer is correct. 

<code>  nlog⁡(n)+n^2+n+log⁡n+1+2^n </code>  
O(c^n) - This answer is correct. 

**Problem 4-1**
Consider the following Python procedure. Specify its order of growth.
      
<code>  def modten(n):
    return n%10 </code>  
          
O(1) - This answer is correct. 

**Problem 4-2**
Consider the following Python procedure. Specify its order of growth.
      
<code>  def multlist(m, n):
    '''
    m is the multiplication factor
    n is a list.
    '''
    result = []
    for i in range(len(n)):
        result.append(m*n[i])
    return result   </code>  
          
O(len(n)) - This answer is correct. 

**Problem 4-3**

Consider the following Python procedure. Specify its order of growth.
      
<code>  def foo(n):
    if n <= 1:
        return 1
    return foo(n/2) + 1 <code>  
 
O(log(n)) - This answer is correct. 

**Problem 4-4**

Consider the following Python procedure. Specify its order of growth.

<code>  def recur(n):
    if n <= 0:
        return 1
    else:
        return n*recur(n-1) </code>  

O(n) - This answer is correct. 

**Problem 4-5**
Consider the following Python procedure. Specify its order of growth.

<code>  def baz(n):
    for i in range(n):
        for j in range(n):
            print i,j  </code>  
        
O(n^2) - This answer is correct. 

**Problem 5**
In lecture, we saw a version of linear search that used the fact that a set of elements is sorted in increasing order. Here is the code from lecture:
  
<code>  def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False </code>  
    
Consider the following code, which is an alternative version of search.
    
<code> def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False </code>  
    
Which of the following statements is correct? You may assume that each function is tested with a list L whose elements are sorted in increasing order; for simplicity, assume L is a list of positive integers.

<code>search</code> and <code>newsearch</code> return the same answers for lists <code>L</code> of length 0, 1, or 2.  - correct

**Problem 6-1**
Answer the questions below based on the following sorting function. If it helps, you may paste the code in your programming environment. Study the output to make sure you understand the way it sorts.
     
<code> def swapSort(L): 
    """ L is a list on integers """
    print "Original L: ", L
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print L
    print "Final L: ", L </code>
      
    
Does this function sort the list in increasing or decreasing order? (items at lower indices being smaller means it sorts in increasing order, and vice versa)

Increasing - correct 
 
**Problem 6-2**
What is the worst case time complexity of swapSort? Consider different kinds of lists when the length of the list is large.

O(n^2) - correct 
 
**Problem 6-3**

If we make a small change to the line for j in range(i+1, len(L)): such that the code becomes:
      
<code>def modSwapSort(L): 
    """ L is a list on integers """
    print "Original L: ", L
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print L
    print "Final L: ", L</code>
       
What happens to the behavior of swapSort with this new code?

<code>modSwapSort</code> now orders the list in descending order for all lists. - correct  
 
**Problem 6-4**
What happens to the time complexity of this modSwapSort?

 Best and worst cases stay the same. - correct 
 