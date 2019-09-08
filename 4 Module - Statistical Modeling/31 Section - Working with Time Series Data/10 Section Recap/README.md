
# Section Recap

## Introduction

In this section, you learned about working with time series data and why it is important to you as a data scientist.

## Objectives
You will be able to:
* Understand and explain what was covered in this section
* Understand and explain why this section will help you become a data scientist

## Key Takeaways

The key takeaways from this section include:
* When you import time series data into Pandas, make sure to use the time/date information as index values using either a Pandas Timestamp or Python DateTime data type
* There are a range of built in functions in Pandas for easily downsampling or upsampling time series data
* Line plots and dot plots can be useful for getting a sense of how a time series data set has changed over time
* Histograms and density plots can be useful for getting a sense of the time independent distribution of a time series data set
* Box and whisker plots per year (or other seasonality period - day, week, month, etc) can be a great way to easily see trends in the distribution of time series data over time
* Heat maps can also be useful for comparing changes of time series data across a couple of dimensions. For example, with months on one axis and years on another they can be a great way to see both seasonality and year on year trends
* A time series is said to be stationary if its statistical properties such as mean and variance remain constant over time
* Most time series models work on the assumption that the time series are stationary (assumption of homoscedasticity)
* Many time series data sets *do* have trends, violating the assumption of homoscedasticity
* Common examples are trends include linear (straight line over time), exponential and periodic. Some data sets also have increasing (or decreasing) variance over time
* Any given data set may exhibit multiple trends (e.g. linear, periodic and reduction in variance)
* Rolling statistics can be used to test for trends to see whether the centrality and/or dispersion of the data set changes over time
* The Dickey Fuller Test is a common test for determining whether a data set contains trends
* Common approaches for removing trends and seasonality include taking a log transform,. subtracting the rolling mean and differencing
* Decomposing allows you to separately view seasonality (which could be daily, weekly, annual, etc), trend and "random" which is the variability in the data set after removing the effects of the seasonality and trend

