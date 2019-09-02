
# Introduction to Variables: Strings and Numeric Types - Lab

## Introduction
Now that we have learned about working with different types of data in Python: strings, numbers (ints and floats), and booleans, let's put that knowledge to the test. In this lab we'll imagine that we were at a nice social gathering and exchanged business cards with a few people. One of the business cards belongs to Art Vandelay, a new travel agent. We want to use our programming skills to format this information correctly. 

## Objectives
You will be able to:
* Understand, explain and use the correct data types for various types of information

## Instructions

The next morning we take out the business card, ready to format it using our programming skills, and here is what we find.

![](https://learn-verified.s3.amazonaws.com/data-science-assets/biz-card-mistakes.jpg)

Yeah, Mr. Vandelay may not be the best person to get to know or the best at designing business cards, but like Mr. Vandelay, we know that people enter incorrect information on forms all the time.

So as data scientists, we often need to clean and organize data before we can make sense of it.  Let's get to work. 

## Solving our First Lab

This is our first lab, and here we'll see that there is some data already provided for us.  Next to the data, we will see a comment indicating what the data should look like after we change it.  

> Comments are indicated in Python by a `#` followed by text. They do not get run and will not affect our code. Here we are using them to show what the intended output should be.

For example, let's say we want to capitalize all of the letters of "art vandlay".  We'll see the following:


```python
"art vandelay" # "ART VANDELAY"
```

> **Reminder:** *to **run** the code in a jupyter notebook, press shift + enter after selecting the cell you would like to run.*

> **Note:** In future labs, Learn will check our code to ensure that we did it correctly.  But for our first lab, this works fine.

To get our output to match the comment we will change it to the following:


```python
"art vandelay".upper() # 'ART VANDELAY'
```

## Get Going with Strings

Our first problem will be to capitalize the first letter of each word in `"art vandelay"`. Find the correct string method to capitlize both names.


```python
art_vandelay = "art vandelay" # 'Art Vandelay'
art_vandelay
```

Now let's uppercase all of the letters of "Ceo".


```python
ceo = "Ceo" # 'CEO'
ceo
```

Next we will need our code to answer a question about our email addresses. Every email address should end with ".com". Find the right string method to check if the email address ends with `".com"` and return `True` or `False` accordingly. 


```python
ends_with_com = "art.vandelay@vandelay.co" # False
ends_with_com
```

As you can see below, the website `"vandelay.com"` is not preceded by `"www."`. We can perform what is called string concatenation to fix this! Use the plus sign, `'+'`, to change the website `'vandelay.com'` to the string `'www.vandelay.com'` by prepending `'www.'`.


```python
web_address = 'vandelay.com' # 'www.vandelay.com'
web_address
```

## Working with Numbers

Finally, Mr. Vandelay gave us his phone number, but he actually has two other phone numbers that are different from the one listed.  All three numbers are basically the same with the exception of the ending. Below, start by coercing the first phone number, which is currently a string, to an `int` and add one. Next do the same to the second phone number but increase it by two.


```python
phone_num_one = "7285553334" # 7285553335
phone_num_one 
```


```python
phone_num_two = "7285553334" # 7285553336
phone_num_two
```

## Summary

In this lab, we practiced working with string methods to operate on and answer questions about strings. We wrote methods that return Booleans and changed strings to integers in order to perform addition. So much of working with data is ensuring that it is properly formatted so we can then operate on it, and in this lab, we saw how to use code to do just that.
