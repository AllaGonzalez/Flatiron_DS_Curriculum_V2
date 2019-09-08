
# Model Fit in Linear Regression

## Introduction

In this lecture, you'll learn how to evaluate your model results, and you'll learn methods to select the appropriate features.

## Objectives
You will be able to:
* Analyze the results of regression and R-squared and adjusted-R-squared 
* Understand and apply forward and backward predictor selection

## R-squared and adjusted-R-squared

Take another look at the model summary output for the `auto-mpg` dataset.

The code below reiterates the steps we've taken before: we've created dummies for our categorical variables and have log-transformed some of our continuous predictors. 


```python
import pandas as pd
import numpy as np
data = pd.read_csv("auto-mpg.csv")

acc = data["acceleration"]
logdisp = np.log(data["displacement"])
loghorse = np.log(data["horsepower"])
logweight= np.log(data["weight"])

scaled_acc = (acc-min(acc))/(max(acc)-min(acc))	
scaled_disp = (logdisp-np.mean(logdisp))/np.sqrt(np.var(logdisp))
scaled_horse = (loghorse-np.mean(loghorse))/(max(loghorse)-min(loghorse))
scaled_weight= (logweight-np.mean(logweight))/np.sqrt(np.var(logweight))

data_fin = pd.DataFrame([])
data_fin["acc"]= scaled_acc
data_fin["disp"]= scaled_disp
data_fin["horse"] = scaled_horse
data_fin["weight"] = scaled_weight
cyl_dummies = pd.get_dummies(data["cylinders"], prefix="cyl", drop_first=True)
yr_dummies = pd.get_dummies(data["model year"], prefix="yr", drop_first=True)
orig_dummies = pd.get_dummies(data["origin"], prefix="orig", drop_first=True)
mpg = data["mpg"]
data_fin = pd.concat([mpg, data_fin, cyl_dummies, yr_dummies, orig_dummies], axis=1)
```


```python
data_ols = pd.concat([mpg, scaled_acc, scaled_weight, orig_dummies], axis= 1)
data_ols.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>mpg</th>
      <th>acceleration</th>
      <th>weight</th>
      <th>orig_2</th>
      <th>orig_3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>18.0</td>
      <td>0.238095</td>
      <td>0.720986</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>15.0</td>
      <td>0.208333</td>
      <td>0.908047</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>18.0</td>
      <td>0.178571</td>
      <td>0.651205</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
#import statsmodels.api as sm
from statsmodels.formula.api import ols
```


```python
outcome = 'mpg'
predictors = data_ols.drop('mpg', axis=1)
pred_sum = "+".join(predictors.columns)
formula = outcome + "~" + pred_sum
```


```python
model = ols(formula= formula, data=data_ols).fit()
model.summary()
```




<table class="simpletable">
<caption>OLS Regression Results</caption>
<tr>
  <th>Dep. Variable:</th>           <td>mpg</td>       <th>  R-squared:         </th> <td>   0.726</td> 
</tr>
<tr>
  <th>Model:</th>                   <td>OLS</td>       <th>  Adj. R-squared:    </th> <td>   0.723</td> 
</tr>
<tr>
  <th>Method:</th>             <td>Least Squares</td>  <th>  F-statistic:       </th> <td>   256.7</td> 
</tr>
<tr>
  <th>Date:</th>             <td>Wed, 21 Aug 2019</td> <th>  Prob (F-statistic):</th> <td>1.86e-107</td>
</tr>
<tr>
  <th>Time:</th>                 <td>12:26:06</td>     <th>  Log-Likelihood:    </th> <td> -1107.2</td> 
</tr>
<tr>
  <th>No. Observations:</th>      <td>   392</td>      <th>  AIC:               </th> <td>   2224.</td> 
</tr>
<tr>
  <th>Df Residuals:</th>          <td>   387</td>      <th>  BIC:               </th> <td>   2244.</td> 
</tr>
<tr>
  <th>Df Model:</th>              <td>     4</td>      <th>                     </th>     <td> </td>    
</tr>
<tr>
  <th>Covariance Type:</th>      <td>nonrobust</td>    <th>                     </th>     <td> </td>    
</tr>
</table>
<table class="simpletable">
<tr>
        <td></td>          <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>Intercept</th>    <td>   20.7608</td> <td>    0.688</td> <td>   30.181</td> <td> 0.000</td> <td>   19.408</td> <td>   22.113</td>
</tr>
<tr>
  <th>acceleration</th> <td>    5.0494</td> <td>    1.389</td> <td>    3.634</td> <td> 0.000</td> <td>    2.318</td> <td>    7.781</td>
</tr>
<tr>
  <th>weight</th>       <td>   -5.8764</td> <td>    0.282</td> <td>  -20.831</td> <td> 0.000</td> <td>   -6.431</td> <td>   -5.322</td>
</tr>
<tr>
  <th>orig_2</th>       <td>    0.4124</td> <td>    0.639</td> <td>    0.645</td> <td> 0.519</td> <td>   -0.844</td> <td>    1.669</td>
</tr>
<tr>
  <th>orig_3</th>       <td>    1.7218</td> <td>    0.653</td> <td>    2.638</td> <td> 0.009</td> <td>    0.438</td> <td>    3.005</td>
</tr>
</table>
<table class="simpletable">
<tr>
  <th>Omnibus:</th>       <td>37.427</td> <th>  Durbin-Watson:     </th> <td>   0.840</td>
</tr>
<tr>
  <th>Prob(Omnibus):</th> <td> 0.000</td> <th>  Jarque-Bera (JB):  </th> <td>  55.989</td>
</tr>
<tr>
  <th>Skew:</th>          <td> 0.648</td> <th>  Prob(JB):          </th> <td>6.95e-13</td>
</tr>
<tr>
  <th>Kurtosis:</th>      <td> 4.322</td> <th>  Cond. No.          </th> <td>    8.47</td>
</tr>
</table><br/><br/>Warnings:<br/>[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.



Let's discuss some key metrics in the light of our output:
- R-squared uses a baseline model which is the worst model. This baseline model does not make use of any independent variables to predict the value of dependent variable Y. Instead it uses the mean of the observed responses of dependent variable Y and always predicts this mean as the value of Y. The mathematical formula to calculate R-squared for a linear regression line is in terms of squared errors for the fitted model and the baseline model. In the formula below, $SS_{RES}$ is the residual sum of squared errors or our model, also known as $SSE$, which is the error between the real and predicted values. $SS_{TOT}$ is the difference between real and mean y values.

### $$ R^2 = 1-\dfrac{SS_{RES}}{SS_{TOT}}=1 - \dfrac{\sum_i (y_i-\hat{y_i})^2}{\sum_i {(y_i-\bar{y_i})^2}}$$

-  The problem with $R^2$ is that, whichever predictor you **add** to your model which will make your model more complex, will increase your $R^2$ value. That is, the model tends to overfit if we only use $R^2$ as our model fitting criterion. This is why train test split is essential and why regularization techniques are used to refine more advanced regression models. Make sure to read [this blogpost](https://www.statisticshowto.datasciencecentral.com/adjusted-r2/) on the difference between the two to get a better sense to why use $R^2_{adj}$ !


## The parameter estimates and p-values

Just like with single linear regression, the parameters or coefficients we're calculating have a p-value or *significance* attached to them. The interpretation of the p-value for each parameter is exactly the same as for single multiple regression: 

> The p-value represents the probability that the coefficient is actually zero.

In the Statsmodels output, the p-value can be found in the column with name $P>|t|$. A popular threshold for the p-value is 0.05, where we $p<0.05$ denotes that a certain parameter is significant, and $p>0.05$ means that the parameter isn't significant.

The two columns right to the p-value column represent the bounds associated with the 95% confidence interval. What this means is that, after having run the model, we are 95% certain that our parameter value is within the bounds of this interval. When you chose a p-value cut-off of 0.05, there is an interesting relationship between the 95% confidence interval and the p-value: If the 95% confidence does not include 0, the p-value will be smaller than 0.05, and the parameter estimate will be significant.

## Which variables are most important when predicting the target?

 Now that you know how predictors influence the target, let's talk about selecting the right predictors for your model. It is reasonable to think that when having many potential predictors (sometimes 100s or 1000s of predictors can be available!) not only will adding all of them in largely increase computation time, it might even lead to inferior $R^2_{adj}$ or inferior predictions in general. There are several ways to approach variable selection, and we'll only touch upon this in an ad-hoc manner in this lesson. The most straightforward way is to run a model with each possible *combination* of variables and see which one results in the best metric of your choice, let's say, $R^2_{adj}$. 
> This is where your combinatorics knowledge comes in handy!

Now, when you know about combinations, you know that the number of combinations can add up really quickly. 


> Imagine you have 6 variables. How many models can you create with 6 variables and all subsets of variables?

You can create:
- 1 model with all 6 variables
- 6 models with just 5 variables: $\dbinom{6}{5}$
- 15 models with just 4 variables: $\dbinom{6}{4}= \dfrac{6!}{2!*4!}=15$
- 20 models with 3 variables: $\dbinom{6}{3}= \dfrac{6!}{3!*3!} = 20$
- 15 models with 2 variables: $\dbinom{6}{2}= \dfrac{6!}{4!*2!} = 15$
- 6 models with 1 variable: $\dbinom{6}{1}$
- And, technically, 1 model with no predictors: this will return a model that simply returns the mean of $Y$.

This means that with just 6 variables, a so-called exhaustive search of all submodels results in having to evaluate *64 models*. Below, we'll describe 2 methods that can be used to select a submodel with the most appropriate features: **stepwise selection** on the one hand, and **feature ranking with recursive feature elimination** on the other hand.

### Stepwise selection with p-values

In stepwise selection, you start with an empty model (which only includes the intercept), and each time, the variable that has an associated parameter estimate with the lowest p-value is added to the model (forward step). After adding each new variable in the model, the algorithm will look at the p-values of all the other parameter estimates which were added to the model previously, and remove them if the p-value exceeds a certain value (backward step). The algorithm stops when no variables can be added or removed given the threshold values. 

For more information, it's worth having a look at the [wikipedia page on stepwise regression](https://en.wikipedia.org/wiki/Stepwise_regression).

Unfortunately, stepwise selection is not readily available a Python library just yet. [This stackexchange post](https://datascience.stackexchange.com/questions/937/does-scikit-learn-have-forward-selection-stepwise-regression-algorithm), however, presents the code to do a stepwise selection in statsmodels.


```python
import statsmodels.api as sm

def stepwise_selection(X, y, 
                       initial_list=[], 
                       threshold_in=0.01, 
                       threshold_out = 0.05, 
                       verbose=True):
    """ Perform a forward-backward feature selection 
    based on p-value from statsmodels.api.OLS
    Arguments:
        X - pandas.DataFrame with candidate features
        y - list-like with the target
        initial_list - list of features to start with (column names of X)
        threshold_in - include a feature if its p-value < threshold_in
        threshold_out - exclude a feature if its p-value > threshold_out
        verbose - whether to print the sequence of inclusions and exclusions
    Returns: list of selected features 
    Always set threshold_in < threshold_out to avoid infinite looping.
    See https://en.wikipedia.org/wiki/Stepwise_regression for the details
    """
    included = list(initial_list)
    while True:
        changed=False
        # forward step
        excluded = list(set(X.columns)-set(included))
        new_pval = pd.Series(index=excluded)
        for new_column in excluded:
            model = sm.OLS(y, sm.add_constant(pd.DataFrame(X[included+[new_column]]))).fit()
            new_pval[new_column] = model.pvalues[new_column]
        best_pval = new_pval.min()
        if best_pval < threshold_in:
            best_feature = new_pval.idxmin()
            included.append(best_feature)
            changed=True
            if verbose:
                print('Add  {:30} with p-value {:.6}'.format(best_feature, best_pval))

        # backward step
        model = sm.OLS(y, sm.add_constant(pd.DataFrame(X[included]))).fit()
        # use all coefs except intercept
        pvalues = model.pvalues.iloc[1:]
        worst_pval = pvalues.max() # null if pvalues is empty
        if worst_pval > threshold_out:
            changed=True
            worst_feature = pvalues.argmax()
            included.remove(worst_feature)
            if verbose:
                print('Drop {:30} with p-value {:.6}'.format(worst_feature, worst_pval))
        if not changed:
            break
    return included
```


```python
result = stepwise_selection(predictors, data_fin["mpg"], verbose = True)
print('resulting features:')
print(result)
```

    Add  weight                         with p-value 1.16293e-107
    Add  acceleration                   with p-value 0.000646572
    Add  orig_3                         with p-value 0.0091813
    resulting features:
    ['weight', 'acceleration', 'orig_3']


Applying the stepwise selection on our small auto-mpg example (just starting with the predictors weight, acceleration and the origin categorical levels), we end up with a model that just keeps weight, acceleration, and orig_3.

### Feature ranking with recursive feature elimination

Scikit-learn also provides a few [functionalities for feature selection](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.feature_selection). Their `Feature Ranking with Recursive Feature Elimination` selects the pre-specified $n$ most important features. This means you must specify the number of features to retail. If this number is not provided, half are used by default. See [here](http://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html) for more information on how the algorithm works.  


```python
#from sklearn.datasets import make_friedman1
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression

linreg = LinearRegression()
selector = RFE(linreg, n_features_to_select = 3)
selector = selector.fit(predictors, data_fin["mpg"])
```

Calling the `.support_` attribute tells you which variables are selected


```python
selector.support_ 
```




    array([ True,  True, False,  True])



Calling `.ranking_` shows the ranking of the features, selected features are assigned rank 1


```python
selector.ranking_
```




    array([1, 1, 2, 1])



By calling `.estimator_` on the RFE object, you can get access to the parameter estimates through `.coef_` and `.intercept`.


```python
estimators = selector.estimator_
print(estimators.coef_)
print(estimators.intercept_)
```

    [ 5.11183657 -5.95285464  1.53951788]
    20.841013816401674


Note that the regression coefficients and intercept are slightly different. This is because only the 3 most important features were used in the model instead of the original 4 features. If you pass `n_features_to_select=4`, you should get the original coefficients.  

### Forward selection using adjusted R-squared

[This resource](https://planspace.org/20150423-forward_selection_with_statsmodels/) provides code for a forward selection procedure (much like stepwise selection, but without a backward pass), but this time looking at the adjusted-R-squared to make decisions on which variable to add in the mode.

## Summary

Congrats! In this lecture, you learned about how you can perform selection methods using p-values and adjusted-R-squared.
