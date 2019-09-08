
# Project: Regression Modeling with the Boston Housing Dataset

## Introduction

In this final lab, you'll apply the regression analysis and diagnostics techniques covered in this section to the famous "Boston Housing" dataset. You performed a detailed EDA for this dataset earlier on, and hopefully, you more or less recall how this data is structured! In this lab, you'll use some of the features in this dataset to create a linear model to predict the house price!

## Objectives
You will be able to:
* Build many linear models with the Boston housing data using OLS
* Analyze OLS diagnostics for model validity 
* Visually explain the results and interpret the diagnostics from Statsmodels 
* Comment on the goodness of fit for a simple regression model

## Let's get started

### Import necessary libraries and load 'BostonHousing.csv' as a pandas dataframe


```python
# Your code here
```

The columns in the Boston housing data represent the dependent and independent variables. The dependent variable here is the median house value `MEDV`. The description of the other variables is available on [KAGGLE](https://www.kaggle.com/c/boston-housing). 

### Inspect the columns of the dataset and comment on type of variables present


```python
# Your code here
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
      <th>crim</th>
      <th>zn</th>
      <th>indus</th>
      <th>chas</th>
      <th>nox</th>
      <th>rm</th>
      <th>age</th>
      <th>dis</th>
      <th>rad</th>
      <th>tax</th>
      <th>ptratio</th>
      <th>b</th>
      <th>lstat</th>
      <th>medv</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.00632</td>
      <td>18.0</td>
      <td>2.31</td>
      <td>0</td>
      <td>0.538</td>
      <td>6.575</td>
      <td>65.2</td>
      <td>4.0900</td>
      <td>1</td>
      <td>296</td>
      <td>15.3</td>
      <td>396.90</td>
      <td>4.98</td>
      <td>24.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.02731</td>
      <td>0.0</td>
      <td>7.07</td>
      <td>0</td>
      <td>0.469</td>
      <td>6.421</td>
      <td>78.9</td>
      <td>4.9671</td>
      <td>2</td>
      <td>242</td>
      <td>17.8</td>
      <td>396.90</td>
      <td>9.14</td>
      <td>21.6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.02729</td>
      <td>0.0</td>
      <td>7.07</td>
      <td>0</td>
      <td>0.469</td>
      <td>7.185</td>
      <td>61.1</td>
      <td>4.9671</td>
      <td>2</td>
      <td>242</td>
      <td>17.8</td>
      <td>392.83</td>
      <td>4.03</td>
      <td>34.7</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.03237</td>
      <td>0.0</td>
      <td>2.18</td>
      <td>0</td>
      <td>0.458</td>
      <td>6.998</td>
      <td>45.8</td>
      <td>6.0622</td>
      <td>3</td>
      <td>222</td>
      <td>18.7</td>
      <td>394.63</td>
      <td>2.94</td>
      <td>33.4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.06905</td>
      <td>0.0</td>
      <td>2.18</td>
      <td>0</td>
      <td>0.458</td>
      <td>7.147</td>
      <td>54.2</td>
      <td>6.0622</td>
      <td>3</td>
      <td>222</td>
      <td>18.7</td>
      <td>396.90</td>
      <td>5.33</td>
      <td>36.2</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Record your observations here 

```

### Create histograms for all variables in the dataset and comment on their shape (uniform or not?)


```python
# Your code here 
```


![png](index_files/index_6_0.png)



```python
# You observations here 

```

Based on this, we preselected some features  for you which appear to be more 'normal' than others.
### Create a new dataset with `['crim', 'dis', 'rm', 'zn', 'age', 'medv']`


```python
# Your code here
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
      <th>crim</th>
      <th>dis</th>
      <th>rm</th>
      <th>zn</th>
      <th>age</th>
      <th>medv</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.00632</td>
      <td>4.0900</td>
      <td>6.575</td>
      <td>18.0</td>
      <td>65.2</td>
      <td>24.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.02731</td>
      <td>4.9671</td>
      <td>6.421</td>
      <td>0.0</td>
      <td>78.9</td>
      <td>21.6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.02729</td>
      <td>4.9671</td>
      <td>7.185</td>
      <td>0.0</td>
      <td>61.1</td>
      <td>34.7</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.03237</td>
      <td>6.0622</td>
      <td>6.998</td>
      <td>0.0</td>
      <td>45.8</td>
      <td>33.4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.06905</td>
      <td>6.0622</td>
      <td>7.147</td>
      <td>0.0</td>
      <td>54.2</td>
      <td>36.2</td>
    </tr>
  </tbody>
</table>
</div>



### Check for linearity assumption for all chosen features with target variable using scatter plots


```python
# Your code here 
```


![png](index_files/index_11_0.png)



![png](index_files/index_11_1.png)



![png](index_files/index_11_2.png)



![png](index_files/index_11_3.png)



![png](index_files/index_11_4.png)



```python
# Your observations here 
```

Clearly, your data needs a lot of preprocessing to improve the results. This key behind a Kaggle competition is to process the data in such a way that you can identify the relationships and make predictions in the best possible way. For now, we'll the dataset untouched and just move on with the regression. The assumptions are _exactly_ all fulfilled, but they still hold to a level that we can move on. 

### Let's do Regression 

Now, let's perform a number of simple regression experiments between the chosen independent variables and the dependent variable (price). You'll do this in a loop and in every iteration, you should pick one of the independent variables. Perform the following steps:

* Run a simple OLS regression between independent and dependent variables
* Plot a regression line on the scatter plots
* Plot the residuals using `sm.graphics.plot_regress_exog()`
* Plot a Q-Q plot for regression residuals normality test 
* Store following values in array for each iteration:
    * Independent Variable
    * r_squared'
    * intercept'
    * 'slope'
    * 'p-value'
    * 'normality (JB)' 
* Comment on each output 


```python
# Your code here
```

    Boston Housing DataSet - Regression Analysis and Diagnostics for formula: medv~crim
    -------------------------------------------------------------------------------------



![png](index_files/index_14_1.png)



![png](index_files/index_14_2.png)



![png](index_files/index_14_3.png)


    Press Enter to continue...
    Boston Housing DataSet - Regression Analysis and Diagnostics for formula: medv~dis
    -------------------------------------------------------------------------------------



![png](index_files/index_14_5.png)



![png](index_files/index_14_6.png)



![png](index_files/index_14_7.png)


    Press Enter to continue...
    Boston Housing DataSet - Regression Analysis and Diagnostics for formula: medv~rm
    -------------------------------------------------------------------------------------



![png](index_files/index_14_9.png)



![png](index_files/index_14_10.png)



![png](index_files/index_14_11.png)


    Press Enter to continue...
    Boston Housing DataSet - Regression Analysis and Diagnostics for formula: medv~zn
    -------------------------------------------------------------------------------------



![png](index_files/index_14_13.png)



![png](index_files/index_14_14.png)



![png](index_files/index_14_15.png)


    Press Enter to continue...
    Boston Housing DataSet - Regression Analysis and Diagnostics for formula: medv~age
    -------------------------------------------------------------------------------------



![png](index_files/index_14_17.png)



![png](index_files/index_14_18.png)



![png](index_files/index_14_19.png)


    Press Enter to continue...



```python
pd.DataFrame(results)
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ind_var</td>
      <td>r_squared</td>
      <td>intercept</td>
      <td>slope</td>
      <td>p-value</td>
      <td>normality (JB)</td>
    </tr>
    <tr>
      <th>1</th>
      <td>crim</td>
      <td>0.15078</td>
      <td>24.0331</td>
      <td>-0.41519</td>
      <td>1.17399e-19</td>
      <td>295.404</td>
    </tr>
    <tr>
      <th>2</th>
      <td>dis</td>
      <td>0.0624644</td>
      <td>18.3901</td>
      <td>1.09161</td>
      <td>1.20661e-08</td>
      <td>305.104</td>
    </tr>
    <tr>
      <th>3</th>
      <td>rm</td>
      <td>0.483525</td>
      <td>-34.6706</td>
      <td>9.10211</td>
      <td>2.48723e-74</td>
      <td>612.449</td>
    </tr>
    <tr>
      <th>4</th>
      <td>zn</td>
      <td>0.129921</td>
      <td>20.9176</td>
      <td>0.14214</td>
      <td>5.71358e-17</td>
      <td>262.387</td>
    </tr>
    <tr>
      <th>5</th>
      <td>age</td>
      <td>0.142095</td>
      <td>30.9787</td>
      <td>-0.123163</td>
      <td>1.56998e-18</td>
      <td>456.983</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Your observations here 

```

Clearly, the results are not very reliable. The best R-Squared is witnessed with `rm`, so in this analysis, this is uour best predictor. 

### How can you improve these results?
1. Preprocessing 

This is where preprocessing of data comes in. Dealing with outliers, normalizing data, scaling values etc. can help regression analysis get more meaningful results from the given data. 

2. Advanced Analytical Methods

Simple regression is a very basic analysis technique and trying to fit a straight line solution to complex analytical questions may prove to be very inefficient. Later on, you'll explore at multiple regression where you can use multiple features **at once** to define a relationship with the outcome. You'll also look at some preprocessing and data simplification techniques and revisit the Boston dataset with an improved toolkit. 

## Level up - Optional 

Apply some data wrangling skills that you have learned in the previous section to pre-process the set of independent variables we chose above. You can start off with outliers and think of a way to deal with them. See how it affects the goodness of fit. 

## Summary 

In this lab, you applied your skills learned so far on a new data set. You looked at the outcome of your analysis and realized that the data might need some preprocessing to see a clear improvement in results. You'll pick this back up later on, after learning about more preprocessing techniques and advanced modeling techniques.
