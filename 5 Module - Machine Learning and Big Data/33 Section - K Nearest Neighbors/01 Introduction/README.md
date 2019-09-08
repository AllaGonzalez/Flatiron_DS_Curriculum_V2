
# K-Nearest Neighbors (KNN) Intro

## Introduction

In this section you'll look at an intuitive algorithm known as K-Nearest Neighbors. KNN is an effective classification and regression algorithm that uses nearby points in order to generate a prediction. 

## Objectives

You will be able to:

* Explain what KNN stands for
* Explain the KNN algorithm at a high level

## KNN 

The K-Nearest Neighbors algorithm works as follows:
1. Choose a point 
2. Find the K-Nearest points
    1. K is a predefined user constant such as 1,2,3,5 or 10.
3. Predict a label for the current point:
    1. Classification - Take the most common class of the k neighbors
    2. Regression - Take the average target metric of the k neighbors
    3. Both classification or regression can also be modified to use weighted averages based on the distance of the neighbors

## Distance Metrics

An incredibly important decision when using the KNN algorithm is determining an appropriate distance metric. As one might expect, this makes a monumental impact to the output of the algorithm. While there are additional distance metrics, such as cosine distance which are left out, you'll get a solid introduction to distance metrics by looking at the standard Euclidean distance and its more generic counterpart, Minkowski distance.

## K-Means

While outside the scope of this section, it is worth mentioning the related K-Means algorithm which uses similar principles as KNN but serves as an unsupervised learning clustering algorithm. In the K-Means algorithm, K represents the number of clusters rather then the number of neighbors. Unlike KNN, K-means is an iterative algorithm which repeats until convergence. Nonetheless, its underlying principle is the same, in that it groups data points together using a distance metric in order to create homogeneous groupings.


## Summary

In this introduction, you got a brief overview of the KNN algorithm and distance metrics. From here, you'll jump straight in to get further details of KNN, practice coding your own implementation and then get an introduction to use pre-built tools within sci-kit learn.
