
# PEP8

## Introduction

PEP stands for Python Enhancement Proposals. Check them out [here](https://www.python.org/dev/peps/)! We'll start by talking about PEP8, which is the Style Guide for Python Code. This discusses many points which are also important for collaboration. Git is useful for sharing and integrating code bases, but if code is poorly written it can still be cryptic and difficult to decipher. By following styling guidelines such as those outlined in PEP8, we can all create more legible code that can be shared in a streamlined fashion.

## Objectives

You will be able to:

* Define the acronym PEP
* Describe several style guidelines for python code

## PEP8 Introductory Notes

Remember that the guidelines in PEP8 are just that: guidelines. The main goal is to make code more readable. Often, projects may have their own style guidelines which should take precedence. Most important of all is consistency. Be consistent with how you format your code and stick to it. With that, here's an overview of some of the most important guidelines from the PEP8 document to start familiarizing yourself with.

## Whitespace

1. Avoid trailing whitespace; its hard to see!
2. Always use whitespace on either side of binary operators like =, ==, !=, >, <, <=, not, in, and, or...
3. If operators with different priorities are used, consider adding whitespace around the operators with the lowest priority(ies). For example, multiplication takes precedence over addition, so we might not include whitespace around the multiplication, helping to indicate that these operations happen first and form a cohesive group.

### Good whitespace usage:


```python
i = 1
i = i + 1
i += 1
x = i*2 - 1
hypot2 = x*x + i*i
c = (x+x) * (i-i)
```

### Bad whitespace usage:


```python
i=1
i=i+1
i +=1
x = i * 2 - 1
hypot2 = x * x + i * i
c = (x + x) * (i - i)
```

## Line Length

As a general rule of thumb, limit all lines of code to 79 characters.


```python
#Below is a verbose list comprehension that is 79 characters long as a silly example
[integer**2+1 for integer in range(1,100) if integer > 20 and integer % 5 == 0]
```

## Variable Names

1. Never use the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), or 'I' (uppercase letter eye) as single character variable names.
     1. In some fonts, these characters are indistinguishable from the numerals one and zero. When tempted to use 'l', use 'L' instead.  
2. Don't use built-in python keywords like list, dict or str as variable names: this is not only a style guideline, it will break your code! 

## Indentation

The importance of indentation in python was introduced in the conditionals lesson. Here are the conventional style guidelines that should be followed:

1. When indenting, use 4 spaces instead of a tab.
    1. Note that Python 3 disallows mixing the use of tabs and spaces for indentation. At some point you'll encounter this error: be on the lookout!
2. Vertically align continuation lines of code.
    1. This gets used for long functions, lists or conditionals

Here are some examples using functions. Functions will be introduced formally in the future so don't worry if the syntax looks unfamiliar. Just keep in mind that there are style conventions associated with functions. Comments have been placed in the code to help guide understanding.

### Good Indentation:


```python
# Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)
    
# Aligned with opening delimiter.
foo = long_function_name("var_one", "var_two",
                         "var_three", "var_four")
```

### Bad Indentation:


```python
# Further indentation required as indentation is not distinguishable.
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)

# Arguments on first line forbidden when not using vertical alignment.
foo = long_function_name("var_one", "var_two",
    "var_three", "var_four")
```

Somewhat similarly, when using operations, keep the operator with the operand:

### Good operator placement:


```python
#Note: this line of code will produce an error (the variables referenced have not been defined)
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```

### Bad operator placement:


```python
#Note: this line of code will produce an error (the variables referenced have not been defined)
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)
```

## Additional Resources

* [PEP Website](https://www.python.org/dev/peps/)
* [PEP8 Page](https://www.python.org/dev/peps/pep-0008/)

## Summary

In this lesson, we introduced you to Python Enhancement Proposals (PEPs),
 documents for the python community meant to describe new features or processes. Specifically, we discussed some of the contents of PEP8, the style guide for python. Follow these guidelines will lead to more readable code that can be shared with collaborators. With that, let's leave you with a poem of sorts: PEP20!

PEP 20 -- The Zen of Python

Beautiful is better than ugly.  
Explicit is better than implicit.  
Simple is better than complex.  
Complex is better than complicated.  
Flat is better than nested.  
Sparse is better than dense.  
Readability counts.  
Special cases aren't special enough to break the rules.  
Although practicality beats purity.  
Errors should never pass silently.  
Unless explicitly silenced.  
In the face of ambiguity, refuse the temptation to guess.  
There should be one-- and preferably only one --obvious way to do it.  
Although that way may not be obvious at first unless you're Dutch.  
Now is better than never.  
Although never is often better than *right* now.  
If the implementation is hard to explain, it's a bad idea.  
If the implementation is easy to explain, it may be a good idea.  
Namespaces are one honking great idea -- let's do more of those!  
