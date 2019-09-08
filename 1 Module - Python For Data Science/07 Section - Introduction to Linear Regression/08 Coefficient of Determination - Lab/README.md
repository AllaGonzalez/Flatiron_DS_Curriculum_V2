
# Coefficient of Determination - Lab

## Introduction
In the previous lesson, we looked at the Coefficient of Determination, what it means and how it is calculated. In this lesson, we shall use the R-Squared formula to calculate it in python and numpy. 

## Objectives

You will be able to:

* Mathematically calculate R-Squared using a toy dataset

* Calculate the coefficient of determination (R-Squared) for a given regression line

* Interpret the value of R-Squared


## Let's get started

Once a regression model is created, we need to decide how "accurate" the regression line is to some degree. 


Here is the equation for R-Squared or the Coefficient of Determination again: 

$$ R^2 = 1- \dfrac{SS_{RES}}{SS_{TOT}} = 1- \dfrac{\sum_i(y_i - \hat y_i)^2}{\sum_i(y_i - \overline y_i)^2} $$
 
 Note that this is also equal to:

$$ R^2 = 1- \dfrac{SS_{RES}}{SS_{TOT}}=\dfrac{SS_{EXP}}{SS_{TOT}} $$
where

- $SS_{TOT} = \sum_i(y_i - \overline y_i)^2$ $\rightarrow$ Total Sum of Squares  
-  $SS_{EXP} = \sum_i(\hat y_i - \overline y_i)^2$ $\rightarrow$  Explained Sum of Squares
- $SS_{RES}= \sum_i(y_i - \hat y_i)^2 $ $\rightarrow$ Residual Sum of Squares

Recall that the objective of $R^2$ is to learn how much of the error is a result in variation in the data features, as opposed to being a result of the regression line being a poor fit.

## Programming R-Squared

Let's calculate R-Squared in Python. The first step would be to calculate the Squared Error. Remember that the Squared Error is the Residual Sum of Squares of the difference between a given line and the actual data points.

Create a function `sq_err()` that takes in y points for 2 arrays, calculates the difference corresponding elements of these arrays, squares, and sums all the differences. The function should return the RSS value you saw earlier.


```python
# Calculate sum of squared errors between regression and mean line 
import numpy as np

def sq_err(y_a, y_b):
    """
    input
    y_a : true y values
    y_b : regression line

    
    return
    squared error between regression and true line (ss_tot)
    """
    pass

# Check the output with some toy data
Y_a = np.array([1,3,5,7])
Y_b = np.array([1,4,5,8])

sq_err(Y_a, Y_b)

# 2
```

Squared error, as calculated above is only a part of the coefficient of determination, Let's now build a function that uses `sq_err()` function above to calculate the value of R-Squared by first calculating SSE, then use this same function to calculate SST (use the mean of $y$ instead of the regression line), and then plug in these values into the R-Squared formula. Perform the following tasks
* Calculate the mean of the `y_real`
* Calculate SSE using `sq_err()`
* Calculate SST using `sq_err()`
* Calculate R-Squared from above values using the given formula



```python
# Calculate Y_mean , squared error for regression and mean line , and calculate r-squared

def r_squared(y_real, y_predicted):
    """
    input
    y_real: real values
    y_predicted: regression values
    
    return
    r_squared value
    """
    pass

# Check the output with some toy data
Y = np.array([1,3,5,7])
Y_pred = np.array([1,5,5,10])

r_squared(Y, Y_pred)

# 0.35
```

This R-Squared value is very low, but remember that it wasn't from real data. So now, we have quite a few functions for calculating slope, intercept, best-fit line, plotting and calculating R-squared. In the next lab, you'll put these all together to run a complete regression experiment.

## Summary
In this lesson, you learned how to calculate the R-Squared value in python and numpy. In the next lab, you will put all the functions from the last few labs together to create a complete DIY regression experiment. 
