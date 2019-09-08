
# Section Recap

## Introduction

In this section, you learned the fundamentals of Linear Algebra. An understanding of Linear Algebra will help you better understand the underlying mathematics behind some machine learning algorithms.

## Objectives
You will be able to:
* Understand and explain what was covered in this section
* Understand and explain why this section will help you become a data scientist

## Key Takeaways

The goal of section 26 was to provide both a conceptual and computational introduction to Linear Algebra - one of the foundational concepts underlying most machine learning models. Some of the key takeaways include:
* Understanding Linear Algebra will provide you a much stronger foundation when learning a range of data science topics - from Support Vector Machines and deep learning through Natural Language Processing and dimensionality reduction techniques like Principle Component Analysis
* One use case for vectors and matrices is for representing and solving systems of linear equations
* A scalar is a single, real number. A vector is a one dimensional array of numbers. A matrix is a 2 dimensional array of numbers. 
* A tensor is a generalized term for an n-dimensional rectangular grid of numbers. A vector is a one-dimensional (first order) tensor, a matrix is a two-dimensional (second order tensor), etc.
* Two matrices can be added together if they have the same shape
* Scalars can be added to matrices by adding the scalar (number) to each element
* Broadcasting allows for the addition of matrices of different shapes by extending the dimensions of the smaller matrix to match the dimensions of the larger one
* To calculate the dot product for matrix multiplication, the first matrix must have the same number of columns and the second has rows.
* Matrix multiplication is distributive and associative, but not commutative
* Operating on NumPy data types is substantially more computationally efficient than performing the same operations on native Python data types
* It is possible to use Linear Algebra in NumPy to solve for a linear regression using the OLS method
* OLS is not computationally efficient, so in practice we usually perform a gradient descent instead to solve a linear regression

