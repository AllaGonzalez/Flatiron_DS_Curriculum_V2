
# K-Nearest Neighbors

## Introduction

In this lesson, you'll learn about the supervised learning algorithm **_K-Nearest Neighbors_**, and how you can use it to make predictions for classification and regression tasks!

## Objectives

You will be able to:

* Implement a basic KNN Algorithm from scratch


## What is K-Nearest Neighbors?

**_K-Nearest Neighbors_** (or KNN, for short) is a supervised learning algorithm that can be used for both **_Classification_** and **_Regression_** tasks. KNN is a distance-based classifier, meaning that it implicitly assumes that the smaller the distance between 2 points, the more similar they are. In KNN, each column acts as a dimension. In a dataset with two columns, we can easily visualize this by treating values for one column as X coordinates and and the other as Y coordinates. Since this is a **_Supervised Learning Algorithm_**, you must also have the labels for each point in our dataset, or else you wouldn't know what to predict!

## Fitting the Model

KNN is unique compared to other classifiers in that it does almost nothing during the "fit" step, and all the work during the "predict" step. During the 'fit' step, KNN just stores all the training data and corresponding labels. No distances are calculated at this point. 

## Making Predictions with K

All the magic happens during the 'predict' step. During this step, KNN takes a point that you want a class prediction for, and calculates the distances between that point and every single point in the training set. It then finds the `K` closest points, or **_Neighbors_**, and examines the labels of each. You can think of each of the K-closest points getting a 'vote' about the predicted class. Naturally, they all vote for the same class that they are. The majority wins out, and the algorithm predicts the point in question as whichever class has the highest count among all of the k-nearest neighbors.

In the following animation, K=3.

<img src='images/knn.gif'>

[gif source](https://gfycat.com/wildsorrowfulchevrotain)

## Distance Metrics

When using KNN, you can use **_Manhattan_**, **_Euclidean_**, **_Minkowski Distance_**, or any other distance metric. Choosing an appropriate distance metric is essential and will depend on the context of the problem at hand.

## Evaluating Model Performance

How to evaluate the model performance depends on whether you're using the model for a classification or regression task. KNN can be used for regression (by averaging the target scores from each of the K-nearest neighbors), as well as for both binary and multicategorical classification tasks. 

Evaluating classification performance for KNN works the same as evaluating performance for any other classification algorithm--you just need a set of predictions, and the corresponding ground-truth labels for each of the points you made a prediction on. You can then compute evaluation metrics such as **_Precision, Recall, Accuracy,_** and **_F1-Score_**. 

## Summary
Great! In the next lab, you'll implement KNN using Python!


```python

```
