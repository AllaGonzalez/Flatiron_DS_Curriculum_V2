
# Maximum Likelihood Estimation and Logistic Regression - Recap

## Introduction

Well done! In this section, you reviewed maximum likelihood estimation and logistic regression. This included some challenging coding including gradient descent which pushed you to think critically regarding algorithm implementation. 
In this recap, you'll review a couple of common key points of confusion.

## Objectives

You will be able to:
* Explain reasoning and intuition behind log-likelihood
* Explain caveats of gradient descent
* Explain logistic regression at a high level

## Log Likelihoods in Maximum Likelihood Estimation

One of the nuances you saw in maximum likelihood estimation was that of log likelihoods. Recall that the purpose of taking log likelihoods as opposed to likelihoods themselves, is that it allows us to decompose the product of probabilities as sums of log probabilities. Analytically, this is essential to calculating subsequent gradients in order to find next steps for our optimization algorithm.

## Local Minimums in Gradient Descent

One of the most important notes from this section is that **gradient descent does not guarantee an optimal solution**. Gradient descent is meant to find optimal solutions, but it only guarantees a local minimum. For this reason, gradient descent is frequently run multiple times, and the parameters with the lowest loss function then being selected for the final model.

## Logistic Regression

After coding logistic regression on your own, you then further investigated tuning such models using regularization. Recall that while precision, recall and accuracy are also useful metrics for evaluating classifiers, determining an appropriate balance between false positives and false negatives will depend on the particular problem application and the relative costs of each. For example, in the context of medical screening, a false negative could be devastating, eliminating the possibility for early intervention of the given disease. On the other hand, in another context, such as finding spam email, the cost of false positives might be much higher then false negatives&mdash;after all, having a spam email sneak its way into your inbox is probably preferable then missing an important time sensitive email because it was marked as spam. Due to these contextual considerations, you as the practitioner are responsible for selecting appropriate tradeoffs.

## Summary

In this lesson, you got a brief review of some of the key concepts from the section. Overall, this section was designed to give you additional practice coding algorithms in python, and a deeper understanding of how iterative algorithms such as logistic regression converge to produce underlying model parameters.
