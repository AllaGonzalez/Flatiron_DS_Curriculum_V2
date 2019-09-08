
# OOP - Recap

## Introduction

In this section you learned about Object Oriented Programming (OOP) as a foundational practice for software development and programming.

## Objectives

You will be able to:
* Summarize the importance of OOP
* Explain class attributes and methods
* Explain `self` in classes
* Explain the __init__ method
* Explain object initialization
* Explain object inheritance

## OOP Overview

In this section you learned all about Object Orientated Programming and how to define classes. Like functions, using classes in your programming can save you a lot of time and repetitive tasks. Classes go further then functions in allowing you to also persist data. After all, class methods are fairly analogous to functions, while attributes add additional functionality, acting as data storage containers. Moreover, classes have additional flexibility through inheritance, allowing you to define various levels of abstraction.

## Class Structures

As you saw, the most basic class definition starts off with:  
```python
class Class_name:
```

From there, you then saw how you can further define methods to the class:  

```python
class Class_name:
    def method1(self):
        pass #ideally a method does something, but you get the point
    def method2(self):
        print('This is a pretty useless second method.')
```

And from there, you learned more about `self` and the `__init__` method. Recall that the `__init__` method allows you to specify required and default parameters for you class instances. Furthermore, `self` then allows you to reference object attributes within class definitions. So for example, you might require a class to have a name and a number when instantiated:  

```python
class Class_name:
    def __init__(self, name, number):
        self.name = name
        self.number = number
    def update_name(self, new_name):
        self.name = new_name
    def update_number(self, new_number):
        self.number = new_number
```

You could also add default behavior, allowing the user to not specify a specify parameter when they instantiate an instance of the class:  



```python
class Class_name:
    def __init__(self, name=None, number=None):
        self.name = name
        self.number = number
    def update_name(self, new_name):
        self.name = new_name
    def update_number(self, new_number):
        self.number = new_number
```

## Creating Instances

Recall that once you define a class, you can then create instances of that class to bring it to life and use it!

For example, you might import the `LinearRegression` class from scikit-learn in order to create a regression model!

Remember, creating an instance of a class would look like this:

```python
from sklearn.linear_model import LinearRegression() #importing our class definition
reg = LinearRegression() #creating an instance of the class
```

Once you create an instance object of the class, you can then use all the methods associated with that class!

## Object Inheritance

Finally, you examined object inheritance. You saw that you can create sub classes. To create a subclass of a another class you simply reference the parent class when defining the child class as in:  

```python
class Child_class(Parent_class):
```

Finally, there was a brief mention of python's `super()` function. While it can be useful, some caution should be warranted here; the `super()` function is substantially different between python 2 and 3, and is not as straightforward as it appears. If you're a Java programmer, `super()` will be familiar to you in many aspects, but still works differently in python. Your not apt to need its functionality early on in your programming, but if you wish to learn more, start by checking out its documentation further [here](https://docs.python.org/3/library/functions.html#super).

## Summary

Congrats! You now have a solid introduction to OOP which will be fundamental for collaboration and writing concise modular code!
