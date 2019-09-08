
# Derivatives: the Chain Rule

## Introduction

So far we have seen that the derivative of a function is the instantaneous rate of change of that function.  In other words, how does a function's output change as we change one of the variables?  In this lesson, you will learn about the chain rule, which will allow you to see how a function's output change as we change a variable that function does not directly depend on.  The chain rule may seem complicated, but it is just a matter of following the prescribed procedure.  Learning about the chain rule will allow you to take the derivative of more complicated functions that we will encounter in machine learning.

## Objectives

You will be able to:
- Understand how the chain rule for derivatives works

## The chain rule

Ok, now let's talk about the chain rule.  Imagine that we would like to take the derivative of the following function:

$$f(x) = (0.5x + 3)^2 $$ 

Doing something like that can be pretty tricky right off the bat.  Lucky for us, we can use the chain rule.  The chain rule is essentially a trick that can be applied when our functions get complicated.  The first step is using functional composition to break our function down. Ok, let's do it.

$$g(x) = 0.5x + 3 $$
$$f(x) = (g(x))^2$$

Let's turn these two into functions while we are at it.


```python
def g_of_x(x):
    return 0.5*x + 3
```


```python
g_of_x(2) # 4
```




    4.0




```python
def f_of_x(x):
    return (g_of_x(x))**2
```


```python
f_of_x(2) # 16
```




    16.0



Looking at both the mathematical and code representations of $f(x)$ and $g(x)$, we can see that the $f(x)$ function wraps the $g(x)$ function.  So let's call $f(x)$ **the outer function**, and $g(x)$ **the inner function**.

```python

def g_of_x(x):
    return 0.5*x + 3
    
def f_of_x(x): # outer function f(x) 
    return (g_of_x(x))**2 #inner function g(x)
    
```

Ok, so now let's begin to take derivatives of these functions, starting with the derivative of $g(x)$, the inner function.

From our rules about derivatives we know that the power rule tells us that the derivative of $g(x) = 0.5x$ is 

$$g'(x) = 1*0.5x^0 = 0.5$$

Now a trickier question is: what is the derivative of our outer function $f(x)$? How does the output of our outer function, $f(x)$, change as we vary $x$? 

Notice that the outer function $f(x)$'s output does not directly vary with $x$. As $f(x)=(g(x))^2$, its output varies based on the output, $g(x)$, whose output varies with $x$.

> ** The chain rule**: In taking the derivative, $\frac{\Delta f}{\Delta x}$ of an outer function, $f(x)$, which depends on an inner function $g(x)$, which depends on $x$, the derivative equals the derivative of the outer function times the derivative of the inner function.  

**Or: **

More generally, if we let $ F(x) = f(g(x)) $

$$ F'(x) = f'(g(x))*g'(x) $$

## Work through our steps

Ok, so that is the chain rule.  Let's apply this to our example.

### 1. Separate the function into two functions

Remember we started with the function $f(x) = (0.5x + 3)^2 $.  Then we used functional composition to split this into two.

$$g(x) = (0.5x + 3)$$
$$f(x) = (g(x))^2$$

### 2. Find the derivatives, $f'(x)$ and $g'(x)$

* as we know $g'(x) = 0.5$
* and $f'(g(x)) = 2*(g(x))^{1} = 2*g(x)$

### 3. Substitute into our chain rule

We have: 
* $ f'(g(x)) = f'g(x)*g'(x) = 2*g(x)*0.5 = 1*g(x)$

Then substituting for $g(x)$, which we already defined, we have: 

$f'(g(x)) = g(x) = (0.5x + 3)$

So the derivative of the function $f(x) = (0.5x + 3)^2 $ is $f'(x) = (0.5x + 3) $

### Say it again

The chain rule is allows us to the rate of change of a function that does not directly depend on a variable, $x$, but rather depends on a separate function, that depends on $x$.  For example, the function $f(x)$ below.

```python

def g_of_x(x):
    return 0.5*x + 3
    
def f_of_x(x): # outer function f(x) 
    return (g_of_x(x))**2 #inner function g(x)
    
```

It does not directly depend on $x$, but it does depend on a function $g(x)$, which varies with different outputs of $x$.  So now we want to take the derivative of $f(x)$.

> Remember, taking a derivative means changing a variable $x$ a little, and seeing the change in the output.  The chain rule allows us to solve the problem of seeing the change in output when our function does not **directly** depend on that changing variable; rather, it depends on **a function ** that depends on a variable.  

We can take the derivative of a function that indirectly depends on $x$, by taking the derivative of the outer function and multiplying it by the derivative of the inner function, or 

$f'(x) = f'(g(x))*g'(x)$

## Try it again

Let's go through some more examples.

$$ f(x) = (3x^2 + 10x)^3$$

> Stop here, and give this a shot on your own.  The answer will always be waiting for you right below, so you really have nothing to lose.  No one will know if you struggle - and it's kinda the point.

### 1. Divide the function into two components 

$$g(x) = 3x^2 + 10x $$
$$f(x) = (g(x))^3$$


### 2. Take the derivative of each of the component functions 

$$g'(x) = 6x + 10 $$
$$f'(x) = 3(g(x))^2$$

### 3. Substitution 

$$f'(x) = f'(g(x))*g'(x) = 3(g(x))^2*(6x+10)$$

Then substituting in $g(x) = 3x^2 + 10x $ we have:

$$f'(x) = 3*(3x^2 + 10x)^2*(6x+10) $$

And we can leave it there for now.

## Summary

In this lesson, we learned about the chain rule.  The chain rule allows us to take the derivative of a function that that comprises of another function that depends on $x$.  We apply the chain by taking the derivative of the outer function and multiplying that by the derivative of the inner function.  We'll see the chain rule in the future when in our work with gradient descent.
