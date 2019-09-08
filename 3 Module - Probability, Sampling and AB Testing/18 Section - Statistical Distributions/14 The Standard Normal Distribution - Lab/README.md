
# The Standard Normal Distribution - Lab

## Introduction

In the previous lesson, you learned about the formula of the z-score, and looked at a few toy examples to explain an observation's standard score for normally distributed data. In this lab, you'll practice by standardizing and visualize some normal distributions.

## Objectives

You will be able to:

* Calculate and interpret z-scores for observations
* Visualize the data before and after standardization to visually inspect the results 

## Let's get started

> A z-score can help identify how many standard deviations above or below the mean a certain observation is. Every time you obtain a z-score, use “above” or “below” in your phrasing.

The yields of apples trees in an orchard has been recorded in the file `yield.csv`. Each observation is recorded by weighing apples from trees (in pounds) and adding their weights. There are 5000 observations in total for this data. 

## Load, visualize and give general comments on the dataset

Use pandas for loading and inspecting the data.


```python
# Import libraries

# Read the yield data as a dataframe

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>39.741234</td>
    </tr>
    <tr>
      <th>1</th>
      <td>39.872055</td>
    </tr>
    <tr>
      <th>2</th>
      <td>44.331164</td>
    </tr>
    <tr>
      <th>3</th>
      <td>46.600623</td>
    </tr>
    <tr>
      <th>4</th>
      <td>40.694984</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Create a plot
```


![png](index_files/index_2_0.png)



```python
# Your comments about the data here

```

## Briefly explain what each value represents in this data set**


```python
# Your answer here

```

## Define the interval bounds where such that the range contains 99% of the observations   

> **Hint**: Recall the empirical rule related to $3\sigma$.


```python
# Perform any calculations necessary here

```


```python
# Write your answer here 

```

## Compute and interpret the z-score for a tree yielding 35 pounds of apples


```python
# Calculate z

```


```python
# Interpret the result

```

## Suppose a tree has a z-score of 1.85. Interpret this z-score. What is the yield of this tree?


```python
# Interpret the z score

```


```python
# Calculate yield

```


```python
# What is the yield ?

```

##  Convert each tree’s yield to a z-score so the new variable is the “z-score for weight”

The units are still the apple trees. For the data set of all z-scores:

* What is the shape? 
* The mean? 
* The standard deviation?


```python
# Give your solution here 

```

    Mean: 0.0
    SD: 1.0



![png](index_files/index_17_1.png)



```python
# Your observations

```

## Summary

In this lab, you practiced your knowledge on the standard normal distribution!
