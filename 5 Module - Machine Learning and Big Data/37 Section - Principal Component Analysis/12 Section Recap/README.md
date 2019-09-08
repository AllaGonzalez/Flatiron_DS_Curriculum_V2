
# PCA - Summary

## Introduction

In this lesson, you'll get a brief recap of key concepts from this section.

## Objectives

You will be able to:
* Highlight key takeaways concerning PCA

## PCA 

* Recall that PCA is a dimensionality reduction technique
* There are four steps to calculating PCA:
    * Center each feature by subtracting the feature mean
    * Calculate the covariance matrix for your normalized dataset
    * Calculate the eigenvectors/eigenvalues for the covariance matrix
        * Reorder your eigenvectors based on their accompanying eigenvalues (descending order to the eigenvalues)
    * Take the dot product of the transpose of the eigenvectors with the transpose of the normalized data
* You can also easily implement PCA using sci-kit learn

## Summary

PCA is an essential tool in your skill set. Use it when you need to compress data, and experiment with its effect on machine learning algorithms as a preprocessing step. With PCA, you've now been exposed to unsupervised learning techniques which do not require labeled data.
