
# SVM Recap

## Introduction

As you saw, support vector machines are another classification tool to add to your repertoire. While computationally expensive, they can be powerful tools providing substantial performance gains in many instances.

## Objectives

You will be able to:

* Recall the importance of the c parameter for SVMs
* Recall common kernel functions and their associated hyperparameters

## Kernel Functions

Probably the number one piece of information worth reviewing is some of the various kernel functions that you can apply:

1. Radial Basis Functions (RBF)
    1. `c`
    2. $\gamma$, which can be specified using keyword `gamma` in sci-kit learn
2. Polynomial Kernel
    1. $\gamma$, which can be specified using keyword `gamma` in sci-kit learn
    2. $r$, which can be specified using keyword `coef0` in sci-kit learn
    3. $d$, which can be specified using keyword `degree` in sci-kit learn
3. Sigmoid Kernel
    1. $\gamma$, which can be specified using keyword `gamma` in sci-kit learn
    2. $r$, which can be specified using keyword `coef0` in sci-kit learn

Also recall that in general, `c` is the parameter for balancing standard accuracy metrics for tuning classifiers versus the decision boundary distance.

## Summary

While it may appear that this section is a bit brief, Support Vector Machines are a powerful algorithm that deserve attention. In many cases, SVMs will have the top performance of out of the box classifiers from sci-kit learn. Moreover, learning to properly tune SVMs using kernels and an appropriate c value is critical. In the upcoming labs and lessons you'll further investigate and apply these concepts.
