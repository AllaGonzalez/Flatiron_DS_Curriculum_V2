
# Introduction to Pipelines

## Introduction

You've learned a substantial number of different supervised and unsupervised learning techniques. Now, it's time to learn about a handy tool used to integrate multiple machine learning processes into a single manageable pipeline.

## Objectives

You will be able to:
- Compare different classification techniques
- Construct pipelines in scikit-learn
- Use pipelines in combination with GridSearchCV

## Why Use Pipelines?

Pipelines are extremely useful tools to write clean and manageable code for machine learning. Recall how we start preparing our data set: we want to clean our data, transform it, potentially use feature selection, and then run a machine learning algorithm. Using pipelines, you can do all these steps in one go!

Pipeline functionality can be found in the scikit-learn library `Pipeline`. Pipelines can be coded in a very simple way:

```python
from sklearn.pipeline import Pipeline
   
pipe = Pipeline([('mms', MinMaxScaler()),
                 ('pca', PCA(n_components=10)),
                 ('tree', tree.DecisionTreeClassifier(random_state=123))])
```

This pipeline will ensure that when running the model on our data, first we'll apply MinMaxscaling on our features. Next, some PCA will be applied to downscale the features (to 10 predictors in this case). Last but not least, a decision tree is applied to the data. Note that the decision tree here is a "default" one.

Next, the model can be fit using

```python
pipe.fit(X_train, y_train)

```

A really good blogpost on the basic ideas of pipelining can be found [here](https://www.kdnuggets.com/2017/12/managing-machine-learning-workflows-scikit-learn-pipelines-part-1.html).


## Integrating Grid Search in Pipelines

Note that the above pipeline simply creates one pipeline for a training set, and evaluates on a test set. Is it possible to create a pipeline that performs grid search? And Cross-Validation? Yes we can!

Some code is shown below. You simply create the pipe the way we did it before. Next, you create a parameter grid. When this is all done, you use the function `GridSearchCV()`, which you've seen before, and specify the pipeline as the estimator and the parameter grid. You also have to define how many folds you'll use in your cross-validation. 

```python
# Create the pipeline
pipe = Pipeline([('scl', MinMaxScaler()),
                ('pca', PCA(n_components=10)),
                ('svm', svm.SVC(random_state=123))])

# Create the grid parameter
grid = [{'svm__kernel': ['poly', 'sigmoid'],
         'svm__C': [0.01, 1, 100],
         'svm__degree0': [2,3,4,5],
         'svm__gamma': [0.001, 0.01]}]

# Create the grid, with "pipe" as the estimator
gridsearch = GridSearchCV(estimator=pipe,
                  param_grid=grid,
                  scoring='accuracy',
                  cv=3)

# Fit using grid search
gridsearch.fit(X_train, y_train)
```

An article with a detailed workflow can be found [here](https://www.kdnuggets.com/2018/01/managing-machine-learning-workflows-scikit-learn-pipelines-part-2.html).

## Summary

Great, this wasn't too difficult! The proof of all this is in the pudding. In the next lab, you'll extensively use this workflow to build several pipelines applying several classification algorithms used in this model. Go over to the lab and start with your practice!
