
# Rules for Derivatives

## Introduction

In the previous lesson, we calculated the derivative by changing our delta to see the convergence around a number as reflected in the table above.  However, mathematicians have derived shortcuts to calculate the derivative. 
You'll learn about these shortcuts in this lesson!

## Objectives

You will be able to:

* Understand the rules for taking the derivative of each term
* Understand how to take the derivative of a function 

## Review of derivatives

From previous lessons, you know that the derivative is the instantaneous rate of change of a function.  We said that the derivative of a function at a certain point is just the slope of the function at that point.  And to calculate that slope of the function at a given point, we make $\Delta x$ value smaller until it approaches zero, and see what our $ \dfrac{\Delta f}{\Delta x} $ converges upon.

For example, we saw the following table: 

| $ \Delta x $        | $ \displaystyle \frac{\Delta y}{\Delta x} $|
| ------------- |:-------------:|
| 1      | 5      |
| .1      | 4.1|
| .01 | 4.01     |
| .001 | 4.001      |


This convergence around one number is called the **limit **.  And we can describe what we see in the above table as the expression: 


 $$ f'(2) = \lim_{\Delta x\to0} \dfrac{\Delta f}{\Delta x} = 4  $$

We read this as the limit of $\dfrac{\Delta f}{\Delta x} $ as  $ \Delta x $ approaches zero equals 4.  So, in general our definition of the derivative is:

$$ f'(x) = \lim_{\Delta x\to0} \frac{\Delta f}{\Delta x}  = \lim_{h\to0} \frac{f(x + h) - f(x)}{h} $$

## Rules for calculating the derivative

Derivative rules allow us not just to evaluate the derivative at a single point, as we have done previously, but across any value of $x$ of the function. The most important rules for derivatives are classified in three groups:
- The power rule
- The constant factor rule
- The addition rule

### The power rule

The first rule for us to learn is the power rule.  The power rule is expressed as the following.  Given the following:

$$f(x) = x^r $$

Then, the derivative is: 
$$ f'(x) = r*x^{r-1} $$

This says that if a variable, $x$, is raised to a exponent $r$, then the derivative of that function is the exponent $r$ multiplied by the variable, with the variable raised to the original exponent minus one.  

Let's see this by way of example, with the function, $f(x) = 6*x $.  Remember that we originally calculated the derivative with our formula: 

$$ f'(x) = \lim_{h\to0} \frac{f(x + h) - f(x)}{h} $$

$$ f'(4) = \lim_{h\to0} \frac{f(4 + h) - f(4)}{h} = 6 $$

$$ f'(8) = \lim_{h\to0} \frac{f(8 + h) - f(8)}{h} = 6 $$

We saw that our rate of change of our linear function $f(x) = 6x $ was always 6.  Since the rate of change is constant for linear functions, the derivative was the same across all values of $x$.


```python
import matplotlib.pyplot as plt
import numpy as np

def jog(miles):
    return 6*miles

fig, ax = plt.subplots(figsize=(7.5,5.5))

x = np.linspace(0, 6, 7)
c1= np.linspace(1,2,20)
c2= np.linspace(4,5,20)

plt.plot(x, jog(x), label = "distance given # hours", marker="|", markersize=12)
plt.plot(c1, jog(c1), label = "slope = 6", color="green")
plt.plot(c2, jog(c2), label = "slope = 6", color="red")

ax.legend(loc='upper left', fontsize='large')
plt.ylabel("distance in miles")
plt.xlabel("number of hours")
plt.show()
```


    <matplotlib.figure.Figure at 0x103919400>


Now let's see how this works with our power rule: 

$$f(x) = 6*x = 6*x^{1} $$

Now applying our rule that for a function with 

$$f(x) = x^r $$ 

$$ f'(x) = r*x^{r-1} $$ 

we see that in this case $r = 1$.  So applying our power rule we have: 

$$f'(x) = r*6*x^{r-1} = 1*6*x^{1-1} = 6*x^{0} = 6 $$

Great!  This is aligns with what our graph shows, as well as our calculation using the original definition of the derivative, $\displaystyle\lim_{\Delta x\to0} \dfrac{\Delta y}{\Delta x}$ .

*Another example*

Let's apply the power rule to another example which we used before: the example where the runner starts a race. Here:

$$f(x) = x^2 $$

$$f'(x) = 2*x^{2-1} = 2*x^1 = 2*x $$

Think about what our calculation for $f'(x)$ is saying about our function.  It says, for our function $f(x) = x^2$, a small change in $x$ produces an increase in $f(x) $ equal to 2 times the $ x $ value.  Or, in other words:
$$ f'(x) = 2*x $$

* So when $ x = 2$ then $f'(2) = 2*2 = 4 $
* When $ x = 5 $, then $ f'(5) = 2*5 = 10$
* And when $ x = 10 $, then $ f'(10) = 2*10 = 20$. 

Note that $x$ represents the number of seconds our runner has run, so negative $x$ doesn't make sense here. But there are numerous examples where input variables can be negative, and the same rules are simply applicable here as well. For example, imagine the same function where $x$ represents temperatures.

- when $x=-2$, then $f'(-2) = -4$
- when $x=-7$, then $f'(-7)=-14$

We won't prove the power rule here.  But hopefully, you can see that it does seem to fit our graph of the function $f(x) = x^2$.  Let's take a look.


```python
def f(x):
    return np.square(x)
fig, ax = plt.subplots(figsize=(9.5,6.5))

x = np.linspace(-3, 6, 100)
c1= np.linspace(1.5,2.5,20)
c2= np.linspace(4.5,5.5,20)
c3= np.linspace(-2.5,-1.5,20)

plt.plot(x, f(x), label = "distance given # seconds")

x_dev = np.linspace(1.5, 3.2, 100)
a1 = 2
a2 = 5
a3 = -2
delta_a=0.001
fprime1 = (f(a1+delta_a)-f(a1))/delta_a 
fprime2 = (f(a2+delta_a)-f(a2))/delta_a 
fprime3 = (f(a3+delta_a)-f(a3))/delta_a 

tan1 = f(a1)+fprime1*(c1-a1)
tan2 = f(a2)+fprime2*(c2-a2)
tan3 = f(a3)+fprime3*(c3-a3)

# plot of the function and the tangent
plt.plot(c1, tan1, color = "green", label="slope = 4")
plt.plot(c2, tan2, color = "red", label="slope = 10")
plt.plot(c3, tan3, color = "orange", label="slope = -4")

ax.legend(loc='upper left', fontsize='large')

plt.ylabel("distance in feet")
plt.xlabel("number of seconds")
plt.show()
```


![png](index_files/index_18_0.png)


It seems reasonable that the slope of the line tangent to a curve is $2*x$.  So our power rule for derivatives looks good.

### The constant factor rule

After learning the power rule, the constant factor is a breeze.  The constant factor addresses how to take the derivative of a function multiplied by a constant. 

So in the above example, we have our function of $f(x) = 6*x$.  Now, the derivative of that function

$$f'(x) = 6 * \frac{\Delta f}{\Delta x} $$

Applying the power rule, we know that $ \frac{\Delta f}{\Delta x}x^1 = x^{1-1} = 1 $, so we have: 

$$f'(x) = 6 * \frac{\Delta f}{\Delta x}x = 6*1 = 6$$

In the general case, we can say, consider the function $a*f(x)$ where $a$ is a constant (that is, is a number and not a variable).  Then 

$$\frac{\Delta f}{\Delta x}(a*f(x)) = a * \frac{\Delta f}{\Delta x}*f(x) $$  

> Now, don't let the fancy equations above confuse you.  The rule simply says if a variable is multiplied by a constant (i.e. a number), then to take the derivative of that term, apply our familiar power rule to the variable and multiply the variable by that same constant.

So given the function: 

$$f(x) = 2x^2 $$


$$f'(x) = 2*\frac{\Delta f}{\Delta x} x^{2} = 2*2*x^{2-1} = 4x^1 = 4x $$

That's the constant factor rule in action.

### The addition rule

So far, all of our functions consisted of only one term.  Remember that a term is a constant or variable that is separated by a plus or minus sign.  For example, the function $f(x)$ below has three terms:
    
$ f(x) = 4x^3 - x^2 + 3x $

To take a derivative of a function that has multiple terms, simply take the derivative of each of the terms individually.  So for the function above, 

$$ f(x) = 4x^3 - x^2 + 3x $$

$$ f'(x) = 12x^2 - 2x + 3  $$  

Do you see what we did there?  We simply applied our previous rules to each of the terms individually and continued to add or subtract the terms accordingly.

## Derivatives Drill

Let's take the last few lines of this lesson to practice these derivative rules.

$$f(x) = 3x^5$$

$$g(x) = 10x$$

$$ z(x) = 10 $$

What are the derivatives of these respective functions?

> Take some time to think through it.  

> Even a pen and paper could be in order.

> Ok, maybe the pen is too far away...Time for the answers.

$$f(x) = 3x^5$$
$$f'(x) = 15x^4$$

$$g(x) = 10x$$
$$g'(x) = 10$$

$$ z(x) = 10  $$
$$ z(x) = 10 * (x^0) $$
$$ z'(x) = 0*10x^{0-1} = 0 $$

So as you can see, we are just applying our rule: 

$$f(x) = x^r $$ 

$$ f'(x) = r*x^{r-1} $$ 

And note that whenever we take the derivative of a constant like the number 10, then the derivative of that constant is 0. This also makes sense when thinking of this visually, as the slope of a constant function is 0!

### Evaluating derivatives

Let's evaluate $f'(x)$, $g'(x)$ and $z'(x)$, each at the value where $x = 3$.

Are you able to determine what the derivatives of each of these functions each will equal when $x = 3$?  We simply substitute x for 3, whenever we see $x$.

So:

$$f'(3) = 15x^4 = 15*3^4 = 15*81 = 1215 $$

$$g'(3) = 10 = 10 $$

$$z'(3) = 0 = 0 $$

### Try again

Let's try a couple more derivatives.

$$f(x) = 3x^3 + 8x + 12$$

$$g(x) = 12x^2 + 4x^2 + 2$$

Ok, now for the derivatives. 

 Let's see it!

$$f(x) = 3x^3 + 8x + 12$$
$$f'(x) = 9x^2 + 8 $$

$$g(x) = 12x^2 + 4x^2 + 2$$
$$g'(x) = 24x + 8x = 32x$$

## Summary

In this section, we learned a different way to calculate the derivative.  The derivative of a function at a given point is still the instantaneous rate of change of that function at that point. Now we have three rules that allow us to calculate our derivative.  The most tricky of these is the power rule, which says that if $f(x) = x^r$, then $ f'(x) = r * x^{r-1} $.

Using our derivative rules, we can now calculate the derivative across the entire function.  So the derivative of $f(x) = 6x $ is always 6, and the derivative of $f(x) = x^2 $ is $f(x) = 2x $.  To evaluate our derivative at a specific value of $x$, we simply plug that value of $x$ into our derivative.  When $f'(x) = 2x$, then $f'(2) = 2*2$.  
