
# Section Recap

## Introduction

In this section, you learned about ensemble methods. This lesson will summarize the key takeaways from this section.

## Objectives
You will be able to:
* Understand and explain what was covered in this section
* Understand and explain why this section will help you become a data scientist

## Key Takeaways

The key takeaways from this section include:
* The delphi technique suggests that multiple independent estimates will be more consistently accurate than any single estimate
* Because of this, ensemble techniques are a powerful way for improving the quality of your models
* Sometimes you'll use model stacking or meta-ensembles where you use of combination of different types of model for your ensemble
* It's also common to have multiple similar models in an ensemble - e.g. a bunch of decision trees
* Bagging (Bootstrap AGGregation) is a technique that leverages Bootstrap Resampling and Aggregation
* Bootstrap resampling uses multiple smaller samples from the test data set to create independent estimates, and aggregation is the combining of those estimates to make predictions
* A random forest is an ensemble method for decision trees using Bagging and the Subspace Sampling Method to create variance among the trees
* With a random forest, for each tree, we sample using 2/3 of the training data and the remaining third is used to calculate the Out-of-Bag Error
* In addition, the Subspace Sampling Method is used to further increase variability by randomly selecting the subset of features to use as predictors for training any given tree
* GridsearchCV is an exhaustive search technique for finding optimal combinations of hyper parameters by calculating for every combination of parameter values you put into the search
* Gradient boosting leverages an ensemble of weak learners (weak models) to create a strong combined model
* Boosting (when compared to random forests) is an iterative rather than independent process, using each model to strengthen the weaknesses of the previous ones
* Two of the most common algorithms for Boosting are Adaboost (Adaptive Boosting) and Gradient Boosted Trees
* Adaboost creates new classifiers by continually influencing the distribution of the data sampled to train each successive tree
* Gradient Boosted Trees are a more advanced boosting algorithm that makes use of Gradient Descent
* XGBoost (eXtreme Gradient Boosting) is one of the top gradient boosting algorithms currently in use
* XGBoost is a stand-alone library that implements popular gradient boosting algorithms in the fastest, most performant way possible

