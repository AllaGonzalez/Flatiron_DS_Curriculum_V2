
# Object Oriented Attributes With Functions - Lab

## Introduction
You've been learning a lot about different parts of object-oriented programming. You've learned about classes and what purpose they serve. You've seen instance objects, instance variables, and instance methods and how these things all work with each other. In this lab, you'll learn what a **domain model** is and how it ties into object-oriented programming.

## Objectives

You will be able to:

* Understand the concept of a domain model
* Create a domain model
* Define instance methods that operate on nested data structures

## What Is a Domain Model?

A domain model is the representation of a real-world concept or structure translated into software. This is a key function of object orientation. So far, your Python classes have been used as blueprints or templates for instance objects of that class. As an example, a Driver class would create driver instance objects, and the class would define a basic structure for what that driver instance object should look like and what capabilities it should have. But a class is only one part of a domain model just as, typically, a driver is only one part of a larger structure.

A domain model is meant to mirror that larger, real-world structure. It is more than just one class, it is an entire environment that often depends on other parts or classes to function properly. So, in keeping with a Driver class, you could use the example of a taxi and limousine service as our domain model. There are many more parts to a service like this than drivers alone. You could imagine dispatchers, mechanics, accountants, passengers, etc., all being part of the structure of this domain model. In a simplified example, you could have instance and class methods handle things like `dispatch_driver`, `calculate_revenue_from_rides`, `service_taxi`, or any other function of a taxi and limousine service.

As you become more fluent in object-oriented programming and our programs become more complex, you will see that the other parts of a domain model like passengers, dispatchers, etc., will be classes of their own which interact with each other. 

In this lab, you'll be using a school as our domain model.

## Creating a Simple School Class

To start, open up the **school.py** file in your text editor of choices such as Atom, Sublime, or a simple notepad program. Within this file, create a `School` class definition which will be initialized with the name of the school.

> **Note:** the next cell imports an extension, `autoreload`, from IPython. The autoreload extension reloads any imported packages when methods from that package are called. While this is inefficient for stable packages such as NumPy which will be static while working in a notebook, the autoreload extension is quite useful when developing a package yourself. That is, you can update a package such as school.py and then test the effects in a notebook; with the autoreload extension, you'll see the effects of your changes to the package reflected. 

>> If you still have trouble with cells reflecting updates to the **school.py** file as you go along, go to the Kernel tab at the top of the jupyter notebook and click "Restart & Run All". This should smoothly run everything up to where you're working.




```python
%load_ext autoreload
%autoreload 2
```


```python
from school import School
```


```python
school = School("Middletown High School")
```

## Updating the __init__ method

Great! Now, update you `School` definition in school.py to also include a `roster` attribute upon initialization. Initialize the `roster` attribute as an empty dictionary. Later, you'll use this empty roster dictionary to list students of each grade. For example, a future entry in the roster dictionary could be `{"9": ["John Smith", "Jane Donahue"]}`).


```python
school = School("Middletown High School") #You must reinstantiate the object since you've modified the class definition!
school.roster #{}
```




    {}



## Adding Methods

### Method 1: `add_student()`
Now add a method `add_student` which takes 2 arguments: a student's full name and their grade level, and updates the roster dictionary accordingly. 


```python
school = School("Middletown High School") #Again, you must reinstantiate since you've modified the class!
school.add_student("Peter Piper", 12)
school.roster #{"12": ["Peter Piper"]}
```




    {12: ['Peter Piper']}



> **Hint:** If you're stuck, don't fret; this one's a little tricky. You need to consider two scenarios.
    1. There is no entry for this grade yet in the roster dictionary:
        1. Add an entry to the roster dictionary with the grade key and a single item list using the name
    2. There is an entry for this grade in the roster dictionary:
        1. Append the current name to the list associated with that grade
        
>> Going further: if you're really ambitious, you can actually combine both of these conditions into a single line using the `.get()` method with dictionaries. Here's the docstring for the `.get()` method:  
get(key[, default])  
    Return the value for key if key is in the dictionary, else default. If default is not given, it defaults to None, so that this method never raises a KeyError.


To make sure your method works for both scenarios, run the cell below.


```python
school.add_student("Kelly Slater", 9)
school.add_student("Tony Hawk", 10)
school.add_student("Ryan Sheckler", 10)
school.add_student("Bethany Hamilton", 11)
school.roster # {9: ["Kelly Slater"], 10: ["Tony Hawk", "Ryan Sheckler"], 11: ["Bethany Hamilton"], 12: ["Peter Piper"]}
```




    {12: ['Peter Piper'],
     9: ['Kelly Slater'],
     10: ['Tony Hawk', 'Ryan Sheckler'],
     11: ['Bethany Hamilton']}



### Method 2: `grade()`
Next, define a method called `grade`, which should take in an argument of a grade and return a list of all the students in that grade. 




```python
#While annoying, you do need to reinstantiate the updated class and repform the previous methods
school = School("Middletown High School") 
school.add_student("Peter Piper", 12)
school.add_student("Kelly Slater", 9)
school.add_student("Tony Hawk", 10)
school.add_student("Ryan Sheckler", 10)
school.add_student("Bethany Hamilton", 11)
#Testing out your new method:
print(school.grade(10)) # ["Tony Hawk", "Ryan Sheckler"]
print(school.grade(12)) # ["Peter Piper"]
```

    ['Tony Hawk', 'Ryan Sheckler']
    ['Peter Piper']


### Method 3: `sort_roster()`
Define a method called `sort_roster` that returns the school's roster where the strings in the student arrays are sorted alphabetically. For instance:
`{9: ["Kelly Slater"], 10: ["Ryan Sheckler", "Tony Hawk"], 11: ["Bethany Hamilton"], 12: ["Peter Piper"]}}`

>**Note:** since dictionaries are unordered, the order of the keys does not matter here, just the order of the student's names within each list.


```python
school.sort_roster()
```




    {12: ['Peter Piper'],
     9: ['Kelly Slater'],
     10: ['Ryan Sheckler', 'Tony Hawk'],
     11: ['Bethany Hamilton']}



## Summary
In this lab, you continued to pracitce OOP, designing a more complex domain model using a School class with a few instance methods and variables. Soon you'll see that domain models can use other classes, instance methods, and instance variables to create more functionality in your programs.
