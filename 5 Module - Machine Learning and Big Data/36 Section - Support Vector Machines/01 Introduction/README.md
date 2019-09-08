
# SVM Introduction

## Introduction

SVM stands for support vector machines. These are a type of classifier which modifies the loss function for optimization to not only take into account overall accuracy metrics of the resulting predictions, but aims to maximize the decision boundary between the data points. In essence, this further helps tune the classifier as a good balance between under-fitting and over-fitting.

## Objectives

You will be able to:

* Define SVM
* Give a high level overview of what SVMs are
* Define and explain about Kernel Functions

## Support Vector Machines

In addition to optimizing for accuracy, support vector machines add a slack component, trading in accuracy to increase the distance between data point and the decision boundary. This provides an interesting perspective which can help formalize the intuitive visual choices a human would make in balancing precision and generalization to strike a balance between over-fitting and under-fitting.


## Kernel Functions

Initially, you'll explore linear support vector machines which divide data points into their respective groups by drawing hyperplanes using the dimensions from the feature space. In practice, these have limitations and the dataset may not be cleanly separable. As a result, kernel functions are an additional tool that can be used. Essentially, kernels reproject data onto a new parameter space using combinations of existing features. From there, the same process of applying the same SVMs process to this transformed space can then be employed.

## Summary

While it may appear that this section is a bit brief, Support Vector Machines are a powerful algorithm that deserve attention. In many cases, SVMs will have the top performance of out of the box classifiers from sci-kit learn. Moreover, learning to properly tune SVMs using kernels and an appropriate c value is critical. In the upcoming labs and lessons you'll further investigate and apply these concepts.
