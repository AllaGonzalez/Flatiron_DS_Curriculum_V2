
# Feature and Model Selection: AIC and BIC

## Introduction

Previously, you've seen how you can select ways of assessing your model fit metrics like MSE, SSE, and $R^2$. These values almost always improve when adding more variables, so if you only use these metrics to determine the optimal features of your model, overfitting is likely. You're going to be introduced to two new measures here: the AIC and the BIC.


## Objectives

You will be able to:

- Understand that both AIC and BIC are information criteria that also can be used to perform model selection
- Understand how AIC and BIC use likelihood

## The AIC

The formula for the AIC, invented by Hirotugu Akaike in 1973 and short for "Akaike's Information Criterion" is given by:

#### $$ \text{AIC} = 2k -2\ln(\hat{L}) $$

Where:
* k : length of the parameter space (i.e. the number of features)
* $\hat{L}$ : the maximum value of the likelihood function for the model

Another way to phrase the equation is:

**AIC(model) = -2 \* log-likelihood(model) + 2 \* (length of the parameter space)**

The AIC is generally used to compare each candidate model. The nice thing about the AIC is that for every model that uses Maximum Likelihood Estimation, the log-likelihood is automatically computed, and as a consequence, the AIC is very easy to calculate.

The AIC acts as a penalized log-likelihood criterion, giving a balance between a good fit
(high value of log-likelihood) and complexity (complex models are penalized more than fairly simple ones). The AIC is unbounded so can take any type of value, but the bottom line is that when comparing models, the model with the **lowest** AIC should be selected.

Note that directly comparing the values of log-likelihood maxima for different models (without including the penalty) is not good enough for model comparison because including more parameters in a model will *always* give rise to an increased value of the maximum likelihood. Due to that reason, searching for the model with maximal log-likelihood
would always lead to the model with the most parameters. The AIC balances this by penalizing for number of parameters, hence searching for models with few parameters but fitting the data well.

In Python, the AIC is built in in Statsmodels and some instances of Scikit learn (such as LassoLarsIC, which you'll use in the lab coming up soon.

## The BIC

The BIC (Bayesian Information Criterion) is very similar to the AIC and emerged as a Bayesian response to the AIC, but can be used for the exact same purposes. The idea is to select the candidate model with the highest probability
given the data. 
This idea can be formalised inside a Bayesian framework, involving prior probabilities on candidate models along with prior densities on all parameters in the models. The penalty is slightly changed and depends on the number of rows to the data set:

$$ \text{BIC} = \ln(n)k - 2\ln(\hat{L}) $$

where:

* $\hat{L}$ and k are the same as the previous model
* n : the number of data points (the sample size)

Another way to phrase the equation is:

**BIC(model) = -2 \* log-likelihood(model) + log(number of observations) \* (length of the parameter space)**

Like the AIC, the **lower** your BIC, the better your model is performing.

## Uses of the AIC and BIC

- Performing feature selection: comparing models with only a few variables and more variables, computing the AIC/BIC and select the features that generated the lowest AIC or BIC
- Similarly, selecting or not selecting interactions/polynomial features depending on whether or not the AIC/BIC decreases when adding them in
- Computing the AIC and BIC for several values of the regularization parameter in Ridge/Lasso models and selecting the best regularization parameter.
- Many more!

## Summary

Great! Let's now practice everything you've learned in this section!
