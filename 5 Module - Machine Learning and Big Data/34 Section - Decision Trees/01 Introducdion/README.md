
# Introduction

## Introduction
This lesson summarizes the topics we'll be covering in this section and why they'll be important to you as a data scientist.

## Objectives
You will be able to:
* Understand and explain what is covered in this section
* Understand and explain why the section will help you to become a data scientist

## Decision Trees

In this section, we're going to introduce another kind of model for predicting values that can be used for both continuous and categorical predictions - decision trees. Despite the fact that they've been around for decades, they are still (in conjunction with ensemble methods that we'll learn about in the next section) one of the most powerful modeling tools available for many kinds of machine learning. They are also highly interpretable when compared to more complex models (it's easy to explain and understand how they make their decisions).

### Introduction to PAC Learning Theory and Supervised Learning

We kick off the section by introducing "Probably Approximately Correct" learning theory - a theory that provides a mathematically rigorous definition of what machine learning is. We'll also dig into what exactly the term "Supervised Learning" means, and where it fits in the overall hierarchy of Machine Learning, Artificial Intelligence, and Data Science.

### Introduction to Decision Trees

We then introduce the idea of decision trees. Decision trees are used to classify (or estimate continuous values) by partitioning the sample space as efficiently as possible into sets with similar data points, until you get to a (close to) homogenous set and can reasonably predict the value for your new data point.

### Entropy and Information Gain

The problem with decision trees is that you could get very different predictions depending on what questions you ask and in what order. The question then is how to come up with the right questions to ask in the decision tree in the right order. In this lesson we introduce the idea of entropy and information gain as mechanisms for selecting the most promising questions to ask in a decision tree.

### ID3 Classification Trees

We then introduce Ross Quinlan's ID3 (Iterative Dichotomiser 3) algorithm for generating a decision tree from a data set.

### Building Trees Using Scikit-learn

Next up, we look at how to build a decision tree using the built in functions available in scikit-learn, and how to test the accuracy of the predictions whether using a simple accuracy measure, AUC, or a confusion matrix. We also show how to use the graph_viz library to generate a visualization of the resulting decision tree.

### Hyperparameter Tuning and Pruning

We then look at some of the hyper parameters available when optimizing a decision tree. For example, if you're not careful, generated decision trees can lead to over fitting of data (perfect match for train, horrible for test). There are a number of hyper parameters you can use when generating a tree to minimize overfitting such as maximum depth or minimum leaf sample size. In this lesson we look at these various "pruning" strategies to avoid overfitting of the data and to create a better model. 

### Regression with CART Trees

Up to this point, all of our examples for decision trees have been classifiers, but decision trees can also be used for regressions. In this lesson we introduce the Classification And Regression Trees (CART) algorithm for regression.

### Regression Trees and Model Optimization

In the final lab of the section, we ask you to do a regression analysis using a CART tree and hyper parameter tuning to predict pricing for the Boston Housing data set, giving you a chance to bring everything you've learned in the section to bear on a specific problem.


## Summary

Decision trees are a highly effective and interpretable approach to machine learning. This section will provide you with the skills to create both classifiers and to perform regression using decision trees and to use hyper parameter tuning to optimize your model fit.


