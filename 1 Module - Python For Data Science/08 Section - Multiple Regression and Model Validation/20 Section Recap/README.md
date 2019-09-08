
# Multiple Regression and Model Validation - Recap

## Introduction

In this section you extended your knowledge of building regression models by adding additional predictive variables and subsequently validating those models. Moreover, you also got a brief introduction to data ethics. Remember that throughout your data work it is essential to consider personal privacy and the potential impacts of the data you have access to. 

## Objectives

You will be able to:

* Outline important concepts for regression
* Discuss current issues in data privacy and ethics


## Regression

In this lesson, you saw a number of techniques and concepts regarding regression. This included the idea of using multiple predictors in order to build a stronger estimator. That said, there were caveats to using multiple predictors. For example, multicollinearity between variables should be avoided. One option for features with particularly high correlation is to simply only use one of these features. This improves model interpretability. In addition, linear regression is also most effective when features are of a similar scale. Typically feature scaling and normalization are used to achieve this. There are also other data preperation techniques such as creating dummy variables for categorical variables, and transforming non-normal distributions using functions such as logarithms. Finally, in order to validate models it is essential to always partition your dataset such as with train-test splits or k-fold cross validation.

## Ethics

Aside from regression, you also took a look at data privacy and ethics. You probably had already heard some of these ideas, but may have not been familiar with GDPR or privacy advocacy groups like the Electornic Frontier Foundation. The digital age has brought a slew of political and philosophical questions to the arena, and there are always fascinating (and disturbing) conversations to be had. Be sure to keep these and other issues at the forefront of your though process, and not simply be dazzled by the power of machine learning algorithms. Ask yourself questions like, "What is the algorithm being used for?" or "What are the ramifications or impact of this analysis/program/algorithm?". 

When Einstein released his theory of relativity, its impact had tremendous benefit in advancing the field of physics yet the subsequent development of the Manhattan project was arguably a great detriment of humanity. To a similar vain, be thoughtful of which planes of thought you are operating on, and always be sure to include an ethical and philosophical perspective of the potential ramifications of your work.

## Summary

In this section you learned about adding multiple predictors to your regression models and various methods for validating those models to ensure they generalized to new data observations.
