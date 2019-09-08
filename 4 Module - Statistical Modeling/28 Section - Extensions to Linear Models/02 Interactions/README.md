
# Interactions

## Introduction

In this section, you'll learn about interactions and how to account for them in regression models.

## Objectives

You will be able to:
- Understand what interactions are
- Understand how to accommodate for interactions in regression

## What are interactions?

In statistics, an interaction is a particular property of three or more variables, where two or more variables *interact in a non-additive manner* when affecting a third variable. In other words, the two variables interact to have an effect that is more (or less) than the sum of their parts. 

This might seem pretty abstract, let's use an example to illustrate this.

Let's assume we're trying to predict weight loss of certain people who took a diet, given two (categorical) predictors: the country, and the type of diet they followed. Have a look at the plot below.

- Considering just the people in the USA and the UK, it seems like the effects of both predictors are additive:
    * Weight loss is bigger in the UK than in the USA.
    * Diet C is more effective than diet A. Diet A is more effective than diet B, which makes diet B the least effective.
- When you look at New Zealand, however, it seems like the average weight loss is somewhere between the weight loss for USA and UK, but people seem to be responding much better to diet A than in the UK

<img src='./images/new_diet_image.png' width="500">

This means that the "Country" and "Diet" affect weight loss in a non-additive matter. If we're mostly interested in the effect of diet on weight loss (which seems to be plausible here), we say that Country is a **confounding factor** of the effect of "Diet" on weight loss.

## Why is it important to account for interactions?

Now that you've seen how interactions work, let's now discuss why it is important to add interaction terms. The reason for that is pretty straightforward: not accounting for them might lead to results that are wrong. You'll also notice that including them when they're needed will increase your $R^2$ value!

In our example, the interaction plot was composed out of categorical predictors (countries and diet type), but interactions can occur between categorical variables or between a mix of categorical variables and continuous variables!

Let's go back to our "cars" data set and look at some interactions we can include there.


```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from itertools import combinations
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("auto-mpg.csv") 
y = data[["mpg"]]
X = data.drop(["mpg", "car name"], axis=1)
```


```python
import pandas as pd
import numpy as np
data = pd.read_csv("auto-mpg.csv") 
data['horsepower'].astype(str).astype(int)

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
mpg = data["mpg"]
data_fin = pd.concat([mpg, data_fin, data["cylinders"], data["model year"], data["origin"]], axis=1)
y = data_fin[["mpg"]]
X = data_fin.drop(["mpg"], axis=1)
```


```python
regression = LinearRegression()
crossvalidation = KFold(n_splits=3, shuffle=True, random_state=1)

baseline = np.mean(cross_val_score(regression, X, y, scoring="r2", cv=crossvalidation))
baseline
```




    0.8322880898272432



See how we built a baseline model using some (log-transformed etc) predictors and some categorical predictors. We didn't properly convert the categorical variables to categorical yet, which we should do in the end, but we want to start with a baseline model and a baseline $R^2$ just to get a sense of what a baseline model looks like.

## Interactions between horsepower and origin

To look at how horsepower and origin interact, you can work as follows. Split the data into 3 data sets, one set per origin. Then fit a model with outcome "mpg" and only horsepower as a predictor and do this for each of the data set. Then plot the data all together and see what the regression lines look like.


```python
origin_1 = data_fin[data_fin["origin"]==1]
origin_2 = data_fin[data_fin["origin"]==2]
origin_3 = data_fin[data_fin["origin"]==3]
origin_1.head()
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
      <th>acc</th>
      <th>disp</th>
      <th>horse</th>
      <th>weight</th>
      <th>cylinders</th>
      <th>model year</th>
      <th>origin</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>18.0</td>
      <td>0.238095</td>
      <td>1.125829</td>
      <td>0.173727</td>
      <td>0.720986</td>
      <td>8</td>
      <td>70</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>15.0</td>
      <td>0.208333</td>
      <td>1.372223</td>
      <td>0.321860</td>
      <td>0.908047</td>
      <td>8</td>
      <td>70</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>18.0</td>
      <td>0.178571</td>
      <td>1.191999</td>
      <td>0.262641</td>
      <td>0.651205</td>
      <td>8</td>
      <td>70</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>16.0</td>
      <td>0.238095</td>
      <td>1.107370</td>
      <td>0.262641</td>
      <td>0.648095</td>
      <td>8</td>
      <td>70</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>17.0</td>
      <td>0.148810</td>
      <td>1.094964</td>
      <td>0.219773</td>
      <td>0.664652</td>
      <td>8</td>
      <td>70</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
regression_1 = LinearRegression()
regression_2 = LinearRegression()
regression_3 = LinearRegression()

horse_1 = origin_1["horse"].values.reshape(-1, 1)
horse_2 = origin_2["horse"].values.reshape(-1, 1)
horse_3 = origin_3["horse"].values.reshape(-1, 1)

regression_1.fit(horse_1, origin_1["mpg"])
regression_2.fit(horse_2, origin_2["mpg"])
regression_3.fit(horse_3, origin_3["mpg"])

# Make predictions using the testing set
pred_1 = regression_1.predict(horse_1)
pred_2 = regression_2.predict(horse_2)
pred_3 = regression_3.predict(horse_3)

# The coefficients
print(regression_1.coef_)
print(regression_2.coef_)
print(regression_3.coef_)
```

    [-25.29729196]
    [-28.17074549]
    [-30.73684923]


You can see that we have three different estimates for the slope,  -25.29 for origin = 1, -28.17 for origin = 2, and -30.74 for origin = 3. It is not unexpected to see that they are slightly different. Now, let's look at the plot.


```python
# Plot outputs
plt.figure(figsize=(10,6))

plt.scatter(horse_1, origin_1["mpg"],  color='blue', alpha = 0.3, label = "origin = 1")
plt.scatter(horse_2, origin_2["mpg"],  color='red', alpha = 0.3, label = "origin = 2")
plt.scatter(horse_3, origin_3["mpg"],  color='orange', alpha = 0.3, label = "origin = 3")

plt.plot(horse_1, pred_1,  color='blue', linewidth=2)
plt.plot(horse_2, pred_2,  color='red', linewidth=2)
plt.plot(horse_3, pred_3,  color='orange', linewidth=2)
plt.ylabel("mpg")
plt.xlabel("horsepower")
plt.legend();
```


![png](index_files/index_20_0.png)


Even though we get three different lines at different levels, they do seem to be more or less parallel, so the effect seems pretty additive. Just based on looking at this, it seems like there is no real interaction and the effect of origin when predicting mpg using horsepower is additive. It might not be necessary to include an interaction effect in our model. But how would actually include interaction effects in our model? To do this, you basically multiply 2 predictors. Let's add an interaction effect between origin and horsepower and see how it affects or $R^2$. 


```python
regression = LinearRegression()
crossvalidation = KFold(n_splits=3, shuffle=True, random_state=1)

X_interact = X.copy()
X_interact["horse_origin"] = X["horse"] * X["origin"]

interact_horse_origin = np.mean(cross_val_score(regression, X_interact, y, scoring="r2", cv=crossvalidation))
interact_horse_origin
```




    0.8416810370430339



By actually including an interaction effect here, we did bump our $R^2$ to 0.841 from 0.832, so about 1%! Let's now run the same model in statsmodels to see if the interaction effect is significant.


```python
import statsmodels.api as sm
X_interact = sm.add_constant(X_interact)
model = sm.OLS(y,X_interact)
results = model.fit()

results.summary()
```




<table class="simpletable">
<caption>OLS Regression Results</caption>
<tr>
  <th>Dep. Variable:</th>           <td>mpg</td>       <th>  R-squared:         </th> <td>   0.856</td> 
</tr>
<tr>
  <th>Model:</th>                   <td>OLS</td>       <th>  Adj. R-squared:    </th> <td>   0.853</td> 
</tr>
<tr>
  <th>Method:</th>             <td>Least Squares</td>  <th>  F-statistic:       </th> <td>   285.6</td> 
</tr>
<tr>
  <th>Date:</th>             <td>Wed, 17 Apr 2019</td> <th>  Prob (F-statistic):</th> <td>2.84e-156</td>
</tr>
<tr>
  <th>Time:</th>                 <td>15:26:07</td>     <th>  Log-Likelihood:    </th> <td> -980.75</td> 
</tr>
<tr>
  <th>No. Observations:</th>      <td>   392</td>      <th>  AIC:               </th> <td>   1980.</td> 
</tr>
<tr>
  <th>Df Residuals:</th>          <td>   383</td>      <th>  BIC:               </th> <td>   2015.</td> 
</tr>
<tr>
  <th>Df Model:</th>              <td>     8</td>      <th>                     </th>     <td> </td>    
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
  <th>const</th>        <td>  -30.5230</td> <td>    4.092</td> <td>   -7.460</td> <td> 0.000</td> <td>  -38.568</td> <td>  -22.478</td>
</tr>
<tr>
  <th>acc</th>          <td>   -3.8734</td> <td>    1.680</td> <td>   -2.306</td> <td> 0.022</td> <td>   -7.177</td> <td>   -0.570</td>
</tr>
<tr>
  <th>disp</th>         <td>   -1.0423</td> <td>    0.738</td> <td>   -1.412</td> <td> 0.159</td> <td>   -2.494</td> <td>    0.409</td>
</tr>
<tr>
  <th>horse</th>        <td>    1.6583</td> <td>    3.342</td> <td>    0.496</td> <td> 0.620</td> <td>   -4.912</td> <td>    8.228</td>
</tr>
<tr>
  <th>weight</th>       <td>   -3.3236</td> <td>    0.610</td> <td>   -5.452</td> <td> 0.000</td> <td>   -4.522</td> <td>   -2.125</td>
</tr>
<tr>
  <th>cylinders</th>    <td>   -0.0596</td> <td>    0.296</td> <td>   -0.201</td> <td> 0.841</td> <td>   -0.642</td> <td>    0.523</td>
</tr>
<tr>
  <th>model year</th>   <td>    0.7318</td> <td>    0.046</td> <td>   16.002</td> <td> 0.000</td> <td>    0.642</td> <td>    0.822</td>
</tr>
<tr>
  <th>origin</th>       <td>   -0.0913</td> <td>    0.331</td> <td>   -0.276</td> <td> 0.783</td> <td>   -0.743</td> <td>    0.560</td>
</tr>
<tr>
  <th>horse_origin</th> <td>   -6.9316</td> <td>    1.446</td> <td>   -4.793</td> <td> 0.000</td> <td>   -9.775</td> <td>   -4.088</td>
</tr>
</table>
<table class="simpletable">
<tr>
  <th>Omnibus:</th>       <td>51.231</td> <th>  Durbin-Watson:     </th> <td>   1.542</td>
</tr>
<tr>
  <th>Prob(Omnibus):</th> <td> 0.000</td> <th>  Jarque-Bera (JB):  </th> <td> 102.044</td>
</tr>
<tr>
  <th>Skew:</th>          <td> 0.725</td> <th>  Prob(JB):          </th> <td>6.94e-23</td>
</tr>
<tr>
  <th>Kurtosis:</th>      <td> 5.036</td> <th>  Cond. No.          </th> <td>2.13e+03</td>
</tr>
</table><br/><br/>Warnings:<br/>[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.<br/>[2] The condition number is large, 2.13e+03. This might indicate that there are<br/>strong multicollinearity or other numerical problems.



Even though the lines look parallel, the interaction effect between horsepower and origin is significant and the R^2 value increased to 0.841.

## Interactions between horsepower and model year

How about interactions between two continuous variables? Let's explore interactions between horsepower and model year. We're interested to see if the effect of horsepower on mpg if different between older cars and younger cars. 


```python
yr_old = data_fin[:180] # cars from 70 to 75
yr_young = data_fin[180:] # cars from 76 to 82
```

What we did here is split the data up to create two data sets, for "older" cars and "younger" cars.


```python
plt.figure(figsize=(12,7))

regression_1 = LinearRegression()
regression_2 = LinearRegression()

horse_1 = yr_old["horse"].values.reshape(-1, 1)
horse_2 = yr_young["horse"].values.reshape(-1, 1)

regression_1.fit(horse_1, yr_old["mpg"])
regression_2.fit(horse_2, yr_young["mpg"])

# Make predictions using the testing set
pred_1 = regression_1.predict(horse_1)
pred_2 = regression_2.predict(horse_2)

# The coefficients
print(regression_1.coef_)
print(regression_2.coef_)
```

    [-21.39522143]
    [-35.10169206]



    <Figure size 864x504 with 0 Axes>



```python
# Plot outputs
plt.figure(figsize=(10,6))

plt.scatter(horse_1, yr_old["mpg"],  color='blue', alpha = 0.3, label = "older cars")
plt.scatter(horse_2, yr_young["mpg"],  color='red', alpha = 0.3, label = "younger cars")

plt.plot(horse_1, pred_1,  color='blue', linewidth=2)
plt.plot(horse_2, pred_2,  color='red', linewidth=2)

plt.ylabel("mpg")
plt.xlabel("horsepower")
plt.legend();
```


![png](index_files/index_31_0.png)


More than for our previous example. there seems to be an interaction between horsepower and cars. Let's add the interaction effect in our model and see how it affects $R^2$. 


```python
regression = LinearRegression()
crossvalidation = KFold(n_splits=3, shuffle=True, random_state=1)

X_interact_2 = X.copy()
X_interact_2["horse_year"] = X["horse"] * X["model year"]

interact_horse_origin = np.mean(cross_val_score(regression, X_interact_2, y, scoring="r2", cv=crossvalidation))
interact_horse_origin
```




    0.8597777940161033



This result confirms what we have seen before: including this interaction has an even bigger effect on the $R^2$. When running this in statsmodels, unsurprisingly, the effect is significant.


```python
import statsmodels.api as sm
X_interact_2 = sm.add_constant(X_interact_2)
model = sm.OLS(y,X_interact_2)
results = model.fit()

results.summary()
```




<table class="simpletable">
<caption>OLS Regression Results</caption>
<tr>
  <th>Dep. Variable:</th>           <td>mpg</td>       <th>  R-squared:         </th> <td>   0.874</td> 
</tr>
<tr>
  <th>Model:</th>                   <td>OLS</td>       <th>  Adj. R-squared:    </th> <td>   0.871</td> 
</tr>
<tr>
  <th>Method:</th>             <td>Least Squares</td>  <th>  F-statistic:       </th> <td>   331.7</td> 
</tr>
<tr>
  <th>Date:</th>             <td>Wed, 17 Apr 2019</td> <th>  Prob (F-statistic):</th> <td>5.05e-167</td>
</tr>
<tr>
  <th>Time:</th>                 <td>15:26:07</td>     <th>  Log-Likelihood:    </th> <td> -955.36</td> 
</tr>
<tr>
  <th>No. Observations:</th>      <td>   392</td>      <th>  AIC:               </th> <td>   1929.</td> 
</tr>
<tr>
  <th>Df Residuals:</th>          <td>   383</td>      <th>  BIC:               </th> <td>   1964.</td> 
</tr>
<tr>
  <th>Df Model:</th>              <td>     8</td>      <th>                     </th>     <td> </td>    
</tr>
<tr>
  <th>Covariance Type:</th>      <td>nonrobust</td>    <th>                     </th>     <td> </td>    
</tr>
</table>
<table class="simpletable">
<tr>
       <td></td>         <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>const</th>      <td>  -30.3764</td> <td>    3.792</td> <td>   -8.010</td> <td> 0.000</td> <td>  -37.832</td> <td>  -22.920</td>
</tr>
<tr>
  <th>acc</th>        <td>   -2.2225</td> <td>    1.575</td> <td>   -1.411</td> <td> 0.159</td> <td>   -5.319</td> <td>    0.874</td>
</tr>
<tr>
  <th>disp</th>       <td>   -0.9066</td> <td>    0.689</td> <td>   -1.315</td> <td> 0.189</td> <td>   -2.262</td> <td>    0.449</td>
</tr>
<tr>
  <th>horse</th>      <td>  120.4052</td> <td>   14.754</td> <td>    8.161</td> <td> 0.000</td> <td>   91.395</td> <td>  149.415</td>
</tr>
<tr>
  <th>weight</th>     <td>   -3.7671</td> <td>    0.561</td> <td>   -6.712</td> <td> 0.000</td> <td>   -4.871</td> <td>   -2.664</td>
</tr>
<tr>
  <th>cylinders</th>  <td>    0.3899</td> <td>    0.260</td> <td>    1.498</td> <td> 0.135</td> <td>   -0.122</td> <td>    0.902</td>
</tr>
<tr>
  <th>model year</th> <td>    0.6736</td> <td>    0.043</td> <td>   15.550</td> <td> 0.000</td> <td>    0.588</td> <td>    0.759</td>
</tr>
<tr>
  <th>origin</th>     <td>    0.6130</td> <td>    0.256</td> <td>    2.396</td> <td> 0.017</td> <td>    0.110</td> <td>    1.116</td>
</tr>
<tr>
  <th>horse_year</th> <td>   -1.7272</td> <td>    0.194</td> <td>   -8.896</td> <td> 0.000</td> <td>   -2.109</td> <td>   -1.345</td>
</tr>
</table>
<table class="simpletable">
<tr>
  <th>Omnibus:</th>       <td>32.600</td> <th>  Durbin-Watson:     </th> <td>   1.580</td>
</tr>
<tr>
  <th>Prob(Omnibus):</th> <td> 0.000</td> <th>  Jarque-Bera (JB):  </th> <td>  67.171</td>
</tr>
<tr>
  <th>Skew:</th>          <td> 0.465</td> <th>  Prob(JB):          </th> <td>2.59e-15</td>
</tr>
<tr>
  <th>Kurtosis:</th>      <td> 4.802</td> <th>  Cond. No.          </th> <td>7.96e+03</td>
</tr>
</table><br/><br/>Warnings:<br/>[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.<br/>[2] The condition number is large, 7.96e+03. This might indicate that there are<br/>strong multicollinearity or other numerical problems.



## Additional resources

- You can use the Python library seaborn plots to visualize interactions as well. Have a look [here](https://blog.insightdatascience.com/data-visualization-in-python-advanced-functionality-in-seaborn-20d217f1a9a6) for more information.

- [This resource](http://www.medicine.mcgill.ca/epidemiology/joseph/courses/EPIB-621/interaction.pdf) walks over multiple examples of regressions with interaction terms. Even though the code is in R, it might give you some additional insights into how interactions work.


## Summary

Great! You now know how to interpret interactions, how to include them in your model and how to interpret them. Obviously, nothing stops you from adding multiple interactions at the same time, and you probably should for many occasions. You'll practice what you learned in the next lab, including interactions 
