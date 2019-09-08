
# Mathematical Notation

## Introduction

In this lesson, we'll learn how to read some of the more common mathematical notation that you'll see when reading equations pertaining to Data Science.

## Objectives

You will be able to:

* Read and understand basic mathematical notation


## Understanding Mathematical Notation

When learning Data Science, running into dense, arcane-looking mathematical equations is an inevitability. For instance, here's an equation for a machine learning algorithm called a _Support Vector Machine_ that you'll learn about later in the course:


$ \LARGE \text{minimize:} $

$$ \LARGE W(\alpha) = - \sum_{i=1}^{\ell}\alpha_i + \frac{1}{2}\sum_{i=1}^{\ell}\sum_{j=1}^{\ell}y_iy_j\alpha_i\alpha_j\textbf{x}_i\textbf{x}_j$$


$ \LARGE \text{subject to:} $ $$ \LARGE \sum_{\substack{i=1 \\ 0\leq\alpha_i\leq C}}^{\ell}y_i \alpha_i = 0 $$


<strong><em>Don't stare at this too long, or else you'll get a nosebleed...</em></strong></center>

At first glance, equations like this often seem impenetrable and impossible to understand. If seeing math like this makes you nervous, don't worry--you're not alone! This is a particularly dense example of mathematical notation, but at the end of the day, it's just a recipe for an algorithm. Whereas we are used to expressing our algorithms in code, mathematicians prefer to use **_Mathematical Notation_**, to express big ideas in small, dense packages full of Greek letters, subscripts, and superscripts. Although these look intimidating in the beginning, they'll seem a lot more manageable once we've learned some basic mathematical notation. 

The first thing to remember is that there are many, many mathematical symbols. **_DO NOT_** bother trying to memorize them--that's a waste of time. Instead, keep a cheat sheet handy! And, as with all things, remember that Google is your friend.  There is no shame in looking it up. As a Junior Data Scientist, you're going to be spending an embarrassing amount of time using Google and Stack Overflow to look up things that you don't know. As a Senior Data Scientist, you'll spend the same amount of time doing this--you just won't be embarrassed by it anymore! 

We've included a cheat sheet in this repo (see below) that you should store in an easy-to-find place on your computer. You'll be using it plenty as a Data Scientist. You'll notice that the cheat sheet also contains examples that go with each notation. Use these to your advantage! Toy examples are your friend. 

The cheat sheet works wonders for most of the symbols included on that document. However, there are two types of notation that are worth examining in more depth: **_Summations_**, and **_Products_**. 

## Sigma Notation (Summations)

In the equation above, you'll notice the following symbol appears:

$$\LARGE \sum $$

This is called **_Sigma Notation_**, and is a way of notating **_Summation_**. 

Consider the following code:

```python
sum_total = 0
n = 5
for i in range(1, n+1):
    sum_total += i
```

This is pretty simple code--just a for-loop that calculates the sum total of every number between 1 and 5, inclusive (meaning it stops after including 5 in the total, not before, which is why we put `n+1` in the range instead of just `n`).

A mathematician would express the same algorithm using the following **_Sigma Notation_**:

$$\LARGE \sum_{n=1}^{5} x $$

Pretty nifty, huh? The equation above says that we should start counting at 1, because we see `n=1` under the summation. We should stop once we've hit 5 (inclusive). Our sum totals the sum of each value of X for each step between `n=1` and up to (and including) `n=5`. 

If we were to write it out explicitly, it would look like:

$$\LARGE \sum_{n=1}^{5} x = 1 + 2 + 3 + 4 + 5 $$

This was the most simple example of summation since we were just adding in the individual value at each step in the example above. However, we can put anything we want to the right of the Sigma symbol, and this will be what happens at each step. For example, let's consider the following code:

```python
def f(x):
    return x**2 - 2

sum_total = 0
n = 5
for i in range(1, n+1):
    sum_total += f(i)
```

In the code above, we have a simple function that returns the square of a number, minus 2. This time, the for loop calculates the sum of that function called on every number between 1 and 5, inclusive.  We can write the exact same thing in Sigma Notation as follows:

$$\LARGE \sum_{n=1}^{5}x^2-2$$

Which, if "unrolled" to show each step, would look like: 

$$\LARGE \sum_{n=1}^{5}x^2-2 = (1^2 - 2) + (2^2 - 2) + (3^2 - 2) + (4^2 - 2) + (5^2 - 2) $$

Finally, let's consider what this looks like when working with arrays. 

Consider the following code:

```python
w = [2.2, 3, -2, 4]
x = [0.25, 0, 1, -2]

sum_total = 0

for i in range(len(w)):
    sum_total += w[i] * x[i]
```

In the above example, we use the counter in our for loop as the index to get each subsequent element out of `w` and `x` and multiply them together. We can denote the same thing with Sigma Notation as follows:

$$\LARGE \sum_{i=1}^{w} w_i x_i $$

**_NOTE:_** Can you spot the difference? In our for loop, our index starts at 0, while in our Sigma Notation, our index starts at 1. In practice, they still mean the same thing--start at the first element in each list, multiply them, and add them to the sum, and then continue until we've done that for every item in the list `w`. The Sigma Notation starts at 1 because mathematicians start counting at 1, whereas programmers start counting at 0. **_Remember this--it'll save you from buggy code later on!_** 

## Pi Notation (Products)

Another common type of notation is **_Pi Notation_**, which works similarly to Sigma Notation. The only real difference here is that Pi Notation multiplies each step, rather than adds them to a total. With our understanding of Sigma Notation, it isn't that hard to figure out an example of Pi Notation. 

```python
total = 1
n = 5

for i in range(1, n+1):
    total *= i + 2
```

In Pi Notation, this would translate to:

$$ \LARGE \prod_{i=1}^{5} i + 2$$

Which, when written out completely, would be:

$$ \LARGE \prod_{i=1}^{5} i + 2 = (1 + 2) * (2 + 2) * (3 + 2) * ( 4 + 2) * ( 5 + 2)$$

As you can see from the example above, there isn't too much of a difference between sigma and pi notation. The only difference is that with Sigma, you add the results of each step, whereas with Pi, you multiply them!

## A Cheat Sheet For the Rest

In the repo containing this notebook, you'll find a PDF document called `full-notation.pdf`. This PDF is a multi-page cheat sheet containing all the Greek letters, as well as other more obscure symbols, and examples of what they mean. Again, don't try to memorize it--just keep this cheat sheet handy for when you need it. In general, we'll make an effort to explain any new mathematical symbols or notation as they come up in future lessons. However, if you're not sure, don't be afraid to use this cheat sheet and Google!

## Summary

In this lesson, we learned about how to read basic Sigma and Pi Notation.


```python

```
