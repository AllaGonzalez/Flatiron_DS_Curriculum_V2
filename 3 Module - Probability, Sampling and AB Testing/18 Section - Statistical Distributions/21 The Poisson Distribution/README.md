
# Poisson Distribution

## Introduction

In this lesson, you'll learn about the **Poisson Distribution** and explore some practical ways you can use it. 

## Objectives

You will be able to:

* Understand and explain the Poisson Distribution and its use cases

## What is the Poisson Distribution?

The **Poisson Distribution** is yet another statistical distribution you can use to answer questions about the probability of a given number of successes, the probability of success and a series of independent trials.  Specifically, the Poisson Distribution allows us to calculate the probability of a given event happening by examining the mean number of events that happen in a given time period.  Given a set time period, we can use the Poisson Distribution to predict how many times a given event will happen over that time period.  To help you better understand this, let's examine a few sample questions that we can answer using the Poisson Distribution. 

### Sample Question 1

An average of 20 customers walks into a store in a given hour.  What is the probability that 25 customers walk into a store in the next hour?

### Sample Question 2

A police officer pulls over an average of 3 people for speeding violations per shift.  What is the probability that the officer will pull over two people for speeding violations during their next shift?

## Understanding the Parameters

In order to use the Poisson Distribution, we only need to know a few parameters:

$\mu$: The average number of successes over a given time period. For instance, the average number of customers that walks into a store in a given hour, or the average number of speeding violations a police officer sees in a shift.

$x$: Our random variable--the number of successes we want to find the probability mass of given our knowledge of $\mu$.


### Relationship to the Binomial Distribution

The Poisson distribution has a special relation to the binomial distribution. The theoretical underpinnings are as follows. Imagine that we take a time period and break it into subintervals that are so small that at most one successful event could occur. We can then imagine that for any of these subintervals, a binomial distribution could apply where there is some probability of the event occurring p, a probability q=1-p that the event does not occur, and a probability of 0 that more than one event occurs. We assume that as we cut time into smaller and smaller intervals, the chance of success should go down. If we take the limit of the binomial distribution as n goes to infinity (more and more subintervals that are progressively smaller), the result is the Poisson distribution.

Binomial Probability Distribution:
$$p(x) = \binom{n}{x}p^x(1-p)^{n-x}$$

$$\lambda = n*p$$

Poisson Probability Distribution: $$p(x) = \frac{\lambda^xe^{-\lambda}}{x!}$$

Also note that lambda $\lambda$ is the now the average number of successes that we anticipate in a given interval--The probability $p$ of success, times the number of intervals $n$. This is then exactly how the Poisson is used in practice--if we know the average number of occurrences in a given interval, what is the probability that the actual number of occurrences is slightly more, slightly less, far more or far less?

### Understanding the Formula

Let's take another look at the formula for the Poisson Probability Distribution:

$$p(x) = \frac{\lambda^xe^{-\lambda}}{x!}$$

In the other statistical distributions we've explored, we were explicitly given the probability of success or failure as one of our parameters. In this example, we are not given this probability--however, we know how likely an event is to occur the mean number of times over a given time period, which means that we actually **do** know the probability--we just need to do some basic calculations to discover this probability. 

For instance, if I know that 6 customers walk into a store per hour, we also know enough to calculate the probability that a customer walks in during a given minute. We do this by just dividing the mean number of customers by the length of our interval! 

$$p = \frac{6}{60} = 0.1$$

There is no expectation that customers will walk into a store in evenly spaced intervals--a customer may walk in every 10 minutes on the dot--however, we may also see 3 customers walk in during the first 5 minutes, 3 more customers 10 minutes later, and no other customers for the rest of the hour.  Remember, these events are independent, and this is also the mean number per hour.  This doesn't mean that we have 6 customers every hour - its possible that we do, but it's also possible that we have 12 customers one hour and no customers the next hour. It's also possible that on in a 10-hour day, 60 customers enter the store during the first hour, and then none for the rest of the day.  If your intuition is telling you that this is possible, but not **_plausible_** because it has a very low probability of happening, you're right--and the probability of this happening is exactly what the Poisson Distribution allows us to calculate!

In light of this, it makes sense for us to calculate the probability that a customer will walk in during **_any given minute_**, which we discovered by just dividing our mean number of customers per hour by the number of minutes in our interval, showing us that the probability of a customer walking in during any given minute is 0.1, or 10%.  This number is our $\lambda$ parameter.

Take a look at the following graph - note the relationship of each line to its given $\lambda$ parameter:

<img src='images/new_poisson.png' width="400">

### The Rest of the Formula

Don't let the other terms in that equation scare you - you've seen them before, and even if you haven't they're quite easy to work with:

$e$: Euler's Constant, which is $e \approx 2.71828$. You may also know this as the base of the natural logarithm system. On calculators, this is the `exp` button.  In python, we can access it by using Numpy's `np.exp()` function. 

$x!$: The factorial of x.  For example, $3! = 3 * 2 * 1 = 6$ 

## Summary

In this lesson, you learned about the Poisson Distribution, the Poisson Probability Formula, and how you can use this distribution to solve real-world problems!


```python

```
