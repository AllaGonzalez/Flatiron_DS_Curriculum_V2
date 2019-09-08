
# Recursive Functions

## Introduction

Python supports recursive functions; functions that call themselves in order to loop.
Recursion is an advanced and somewhat uncommon practice in Python as other looping patterns are often simpler, and faster. That said, recursive functions are very useful for traversing unknown shapes and structures.  

## Objectives
You will be able to:
* Understand and use the concept of a recursive function 
* Understand scope in the context of recursive functions
* Understand and compare depth first versus breadth first searches

## A Recursive Example


Let's take a look at a simple case to start.


```python
def mysum(L):
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])
mysum([1,2,3,4,5,6,7,8,9])
```




    45



This function takes a list of numbers and recursively calls itself to add the next item to a summation. The first condition `if not L` allows us to terminate the recursive function; when the list is empty we add 0 to our sum and terminate, as no more recursive calls are made. To better understand this, let's add a couple of print statements to our function.


```python
def mysum(L):
    print(L)
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])

mysum([1,2,3,4,5,6,7,8,9])
```

    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    [2, 3, 4, 5, 6, 7, 8, 9]
    [3, 4, 5, 6, 7, 8, 9]
    [4, 5, 6, 7, 8, 9]
    [5, 6, 7, 8, 9]
    [6, 7, 8, 9]
    [7, 8, 9]
    [8, 9]
    [9]
    []





    45



## Scopes

Each new call to your function creates a new local scope. In other words, this creates a new namespace for the variables within that function call. This can be seen above as our `print(L)` statement continually shows L within the local context of that particular function call. 

## Alternatives

In this case, a summation problem could be easily replaced by using a while loop. This eliminates the need to define function that then makes recursive calls to itself (which creates new scopes). In practice, this can also increase execution performance time.


```python
L = [1,2,3,4,5,6,7,8,9]
sum_1 = 0 
while L:
    sum_1 += L[0]
    L = L[1:]
sum_1
```




    45



You could also use a fairly simple for loop:


```python
L = [1,2,3,4,5,6,7,8,9]
sum_1 = 0 
for x in L:
    sum_1 += x
sum_1
```




    45



## Handling More General Data Structures

Imagine you want our mysum() function to sum nested lists, or arbitrary shape and depth. In other words, your list might contain numbers, lists of numbers, lists of lists of numbers, etc. If you want to write such a function, your simple while or for loop will no longer suffice. Observe:


```python
L = [1,[2,3,4],5,[6,[7,8],9]]
sum_1 = 0 
for x in L:
    sum_1 += x
sum_1
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-5-69d60388f646> in <module>()
          2 sum_1 = 0
          3 for x in L:
    ----> 4     sum_1 += x
          5 sum_1


    TypeError: unsupported operand type(s) for +=: 'int' and 'list'


You get an error because when you try to add the second item, python is unable to add a int and a list; the two are seperate data types. Your recursive function however, does just as good a job by successively iterating through our nested data:


```python
def mysum(L):
    print(L)
    if not L:
        return 0
    elif type(L[0]) == list:
        return mysum(L[0]) + mysum(L[1:])
    else:
        return L[0] + mysum(L[1:])
    
L = [1,[2,3,4],5,[6,[7,8],9]]
mysum(L)
```

    [1, [2, 3, 4], 5, [6, [7, 8], 9]]
    [[2, 3, 4], 5, [6, [7, 8], 9]]
    [2, 3, 4]
    [3, 4]
    [4]
    []
    [5, [6, [7, 8], 9]]
    [[6, [7, 8], 9]]
    [6, [7, 8], 9]
    [[7, 8], 9]
    [7, 8]
    [8]
    []
    [9]
    []
    []





    45



In general, recursive functions can also often be replaced with stacks which determine a queue for successive function calls. See the resources below which adds some more context on this.

## More on Scopes

Notice how you can add a second branch in the conditional logic to further recurse on nested lists. You can also see how this works in practice by the print statements. The scope of L is redefined when the function then reaches the second item at index 1; the nested list [2,3,4]. Once there, the function makes a recursive call to the mysum function of this smaller list and successively see printouts for [2,3,4], [3,4]], [4] and [] as the mysum() function continues to sum this list within the master list.

## Depth Vs. Breadth First Traversals

Another important concept to touch upon and address at this point is the difference between depth and breadth first search trees. The above example demonstrates depth first approach; when mysum hit the second item which was a nested list, it continued all the way down the rabbit hole before moving on. A breadth first search would be if the function processed everything at the first level, putting nested lists on hold till later. Here's the same function rewritten as a breadth first traversal:


```python
#Process everything layer by layer. 
#Thus you process everything in the list, and put off items for later processing if they are nested data structures.
def mysum(L, tot=0):
    print(L)
    deeper_data = [] #Initialize a container for nested data you come across
    #Process the current depth layer
    for i in L:
        if type(i) != list:
            tot += i #If its not a list, its a number! Add it up!
        else:
            [deeper_data.append(j) for j in i] #Add nested items to our list of things to process later on
            #Notice you're digging in a layer here by iterating 
            #through i which you know is a nested data structure from our conditional
    if deeper_data != []:
        return mysum(deeper_data, tot=tot)
        #If you have deeper_data we got to iterate!
    else:
        return tot
        #If you don't have nested data, we're done!
    
L = [1,[2,3,4],5,[6,[7,8],9]]
mysum(L)
```

    [1, [2, 3, 4], 5, [6, [7, 8], 9]]
    [2, 3, 4, 6, [7, 8], 9]
    [7, 8]





    45



## Additional Resources

Check out the link below for a further discussion about depth versus breadth first searches!  

https://brilliant.org/wiki/depth-first-search-dfs/

## Summary
Recursive functions make calls to themselves. Each call defines new scopes for variables and functions within these recursive calls. Although recursive functions are useful for traversing unknown data structures, usually standard `for` and `while` loops will have faster execution. Execution time and readability are important to consider whenever you decide to write a recursive function. Now it's time for you to practice and write some recursive functions on your own!
