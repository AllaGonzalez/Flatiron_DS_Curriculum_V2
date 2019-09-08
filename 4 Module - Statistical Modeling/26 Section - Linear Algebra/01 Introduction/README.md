
# Introduction

## Introduction
In this section, you'll learn about Linear Algebra and why it is important to its fundamentals as a data scientist.

## Objectives
You will be able to:
* Understand and explain what is covered in this section
* Understand and explain why the section will help you to become a data scientist

## Under the Hood - Introducing Linear Algebra

In the first module, we learned the basics of Python - including key data science libraries like NumPy, Pandas, Matplotlib, Statsmodels and Scikit-learn. We got an introduction to SQL for data retrieval and the principles of OO programming. We also learned some key concepts related to probability and statistics. Finally we pulled it all together with an end to end project doing Exploratory Data Analysis & visualization, data cleanup and modeling with multiple predictor values to perform a linear regression.

In this section, we're going to take a step back to learn some of the basics of linear algebra - the math that powers most machine learning models. You may not need to understand linear algebra just to call a method in sklearn to do some modeling, but this introduction to linear algebra should give you a much better understanding of how your models are working "under the hood".

### The Importance of Linear Algebra

We're going to kick this section off by looking at some of the many places that linear algebra is used in machine learniing - from deep learning through Natural Language Processing and dimensionality reduction techniques such as Principle Component Analysis.

### Systems of Linear Equations

We then start to dig into the math! We look at the idea of linear simultaneous equations - a set of two or more equations each of which is linear (can be plotted on a graph as a straight line). We then see how such equations can be represented as vectors or matricies to represent such systems efficiently.

### Scalars, Vectors, Matrices and Tensors

In a code along, we'll then introduce the concepts and concrete representations (in NumPy) of scalars, vectors, matrices and tensors.

### Vector/Matrix Addition and Broadcasting in NumPy

We then start to build up the basic skills required to perform matrix addition and broadcasting (a technique for performing addition on arrays of different shapes). To help you to solidify your understanding we have a lab where you get to practice working with vectors and matrices in NumPy.

### Vector/Matrix Multiplication

We then dig into how to perform multiplication on vectors and matrices - another key technique used by many machine learning models to perform their calculations, covering both the Hadamard product and the (more common) dot product, and give you some exercises to prove the distributive, associative and commutative properties as they relate to matrix multiplication.

### NumPy and Performance

One of the main reasons that NumPy is the default mechanism that most data scientists use for storing and transforming data within Python (as opposed to native Lists and Dictionaries) is its computational efficiency. By getting you to calculate dot-products for modestly sized matrices, you get to experience the difference in performance between NumPy and raw Python data types.

### Solving Systems of Linear Equations using NumPy

We then bring the previous work together to look at how to use NumPy to solve systems of linear equations, introducing the identity and inverse matrices along the way.


### Regression Analysis Using Linear Algebra and NumPy

Now that we have a basic mathematical and computational foundation for linear algebra, it's time to solve a real data problem - looking at how to use NumPy to solve a linear regression using the Ordinary Least Squares method.

### Computational Complexity

Finally, we look at the idea of computational complexity and Big-O notation, showing that while OLS is computationally inefficient, a gradient descent algorithm can be used to solve a linear regression much more efficiently.

 

## Summary

Linear Algebra is so foundational to machine learning that you're going to see it referenced many times as the course progresses. In this section, the goal is to give you both a theoretical introduction and some computational practice, solving a realistic problem by writing the code required to solve a linear regression using OLS.

