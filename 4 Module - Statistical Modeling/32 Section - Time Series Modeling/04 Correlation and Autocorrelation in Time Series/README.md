
# Correlation and Autocorrelation in Time Series

## Introduction

In this lecture, we'll look at correlation,  autocorrelation and partial autocorrelation in time series. 

## Objectives

You will be able to:
- Understand correlation in Time Series
- Plot and discuss the autocorrelation function (ACF) for a time-series 
- Plot and discuss the partial autocorrelation function (PACF) for a time-series 
- Interpret ACF and PACF and Identify use cases both functions

## Correlated Time Series

As you've seen before, correlation is a statistical technique that shows whether and how strongly pairs of variables are related to each other. For correlated variables, you've seen that the Pearson correlation coefficient can be used to summarize the correlation between the variables.

Knowing this, it's no surprise that time series can be correlated as well. To introduce the concept of correlated time series, we use a data set also used in this [blog post](https://www.datacamp.com/community/tutorials/time-series-analysis-tutorial) on www.datacamp.com. The data set contains Google Trends data of three keywords: Diet, Gym and Finance. Let's visualize this time series data.


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
```


```python
gtrends  =  pd.read_csv('google_trends.csv', skiprows=1)
gtrends.head()
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
      <th>Month</th>
      <th>diet: (Worldwide)</th>
      <th>gym: (Worldwide)</th>
      <th>finance: (Worldwide)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2004-01</td>
      <td>100</td>
      <td>31</td>
      <td>47</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2004-02</td>
      <td>77</td>
      <td>27</td>
      <td>49</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2004-03</td>
      <td>75</td>
      <td>25</td>
      <td>47</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2004-04</td>
      <td>73</td>
      <td>24</td>
      <td>47</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2004-05</td>
      <td>75</td>
      <td>23</td>
      <td>44</td>
    </tr>
  </tbody>
</table>
</div>




```python
gtrends.columns = ['Month', 'Diet', 'Gym', 'Finance']
gtrends.Month = pd.to_datetime(gtrends.Month)
gtrends.set_index('Month', inplace=True)
```


```python
gtrends.plot(figsize=(18,6))
plt.xlabel('Year', fontsize=14);
```


![png](index_files/index_4_0.png)


These time series seem to exhibit some seasonality as well. Do you see what's happening? Especially for "Diet" and "Gym" there seems to be a peak in the beginning of each year. The famous New Year's Resolutions!

Not surprisingly, these two seem to move in similar directions at same times as well. We can use the .corr-function 



```python
gtrends.corr()
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
      <th>Diet</th>
      <th>Gym</th>
      <th>Finance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Diet</th>
      <td>1.000000</td>
      <td>-0.050934</td>
      <td>-0.026604</td>
    </tr>
    <tr>
      <th>Gym</th>
      <td>-0.050934</td>
      <td>1.000000</td>
      <td>-0.223186</td>
    </tr>
    <tr>
      <th>Finance</th>
      <td>-0.026604</td>
      <td>-0.223186</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>



Interestingly, The correlations do not seem to be big, and have negative signs. But when we look at the plots, there is clearly some similar movements. What are we doing wrong?

Remember how we said that we want to make our time series **stationary**? This is where you can show off your detrending skills! Turns out you can more easily find out if time series are correlated if you **detrend** them first. Let's use differencing to detrend these time series and then calculate the correlation again!


```python
gtrends_diff = gtrends.diff(periods=1)
```


```python
gtrends_diff.plot(figsize=(18,6))
plt.xlabel('Year', fontsize=14);
```


![png](index_files/index_9_0.png)



```python
gtrends_diff.corr()
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
      <th>Diet</th>
      <th>Gym</th>
      <th>Finance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Diet</th>
      <td>1.000000</td>
      <td>0.793339</td>
      <td>0.395105</td>
    </tr>
    <tr>
      <th>Gym</th>
      <td>0.793339</td>
      <td>1.000000</td>
      <td>0.341564</td>
    </tr>
    <tr>
      <th>Finance</th>
      <td>0.395105</td>
      <td>0.341564</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>



So how did this happen? The spikes at the beginning of the year are a form of **seasonality**. By using 1-lag differencing you eliminated the simple trend, without getting rid of the seasonality. The trend "confused" the correlation coefficient, but after differencing, the correlation is very apparent.

## Autocorrelation

Autocorrelation is a very powerful tool for time series analysis. it helps us study how each time series observation is related to its recent (or not so recent) past. processes with greater autocorrelation are more predictable than those without any form of autocorrelation.

Let's start with comparing the time series of the keyword "Diet", with the time series with a lag of one. What you're essentially doing, is your comparing each value in the time series, with yesterday's value (or in case of the "Diet" series, with the value in the previous month. This is called "lag 1 autocorrelation".

You can use the `.shift` function in pandas to shift the index forward, or backward.


```python
diet = gtrends[['Diet']]
```


```python
diet_shift_1 = diet.shift(periods=1)
diet_shift_1.head()
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
      <th>Diet</th>
    </tr>
    <tr>
      <th>Month</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2004-01-01</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2004-02-01</th>
      <td>100.0</td>
    </tr>
    <tr>
      <th>2004-03-01</th>
      <td>77.0</td>
    </tr>
    <tr>
      <th>2004-04-01</th>
      <td>75.0</td>
    </tr>
    <tr>
      <th>2004-05-01</th>
      <td>73.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
lag_1= pd.concat([diet_shift_1, diet], axis=1)

lag_1.corr()
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
      <th>Diet</th>
      <th>Diet</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Diet</th>
      <td>1.000000</td>
      <td>0.624862</td>
    </tr>
    <tr>
      <th>Diet</th>
      <td>0.624862</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>



Let's plot them together to get a sense of what's happening


```python
lag_1.plot(figsize=(18,6))
```




    <matplotlib.axes._subplots.AxesSubplot at 0x120be0a58>




![png](index_files/index_16_1.png)


You can see that the "lag 1 autocorrelation" is 0.62. Let's look at lag 2:


```python
diet_shift_2 = diet.shift(periods=2)

lag_2= pd.concat([diet_shift_2, diet], axis=1)

lag_2.corr()
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
      <th>Diet</th>
      <th>Diet</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Diet</th>
      <td>1.000000</td>
      <td>0.537913</td>
    </tr>
    <tr>
      <th>Diet</th>
      <td>0.537913</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>



The "lag 2 autocorrelation" is 0.54, so a little lower than the "lag 1 autocorrelation".

Now, how about a lag 12 autocorrelation?


```python
diet_shift_12 = diet.shift(periods=12)

lag_12= pd.concat([diet_shift_12, diet], axis=1)

lag_12.corr()
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
      <th>Diet</th>
      <th>Diet</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Diet</th>
      <td>1.000000</td>
      <td>0.754955</td>
    </tr>
    <tr>
      <th>Diet</th>
      <td>0.754955</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>



Unsurprisingly, this autocorrelation is high! We're basically comparing the series shifting our data 1 year, so January 2004 is compared to January 2005, and so on. Let's visualize these series and the 12-lag shifted series as well.


```python
lag_12.plot(figsize=(18,6))
```




    <matplotlib.axes._subplots.AxesSubplot at 0x11fc33198>




![png](index_files/index_23_1.png)


## The Autocorrelation Function

Great, but wouldn't it be nice to get a summary of the autocorrelations for each lag? Well, that's exactly what the **autocorrelation function** (often abbreviated to ACF) does. The autocorrelation function is a function that represents autocorrelation of a time series as a function of the time lag.

The correlation function tells interesting stories about trends and seasonality. For example, if the original time series repeats itself every five days, you would expect to see a spike in the autocorrelation function at 5 days.

Creating an autocorrelation function for our "Diet" series, we you have the lag on the x-axis and the correlation value for each respective lag value on the y-axis. 

You can use the `autocorrelation_plot` function in Pandas' `plotting` module.


```python
plt.figure(figsize=(12,5))
pd.plotting.autocorrelation_plot(diet);
```


![png](index_files/index_25_0.png)


Look at that, you can clearly identify spikes for lags of multiples of 12. However, The dotted lines in the plot tell you about the statistical significance of the correlation. For these time series, you can say that 'Diet' is definitely autocorrelated for lags of twelve months and 24 months, but for some later lags the result is not significant.

Like before, instead of plotting the autocorrelation function for the "Diet" series as is, we can also plot the autocorrelation function for the differenced series. Let's see how that changes our result.


```python
diet_diff = gtrends_diff[["Diet"]].dropna()
```


```python
plt.figure(figsize=(12,6))
pd.plotting.autocorrelation_plot(diet_diff)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x1c24083dd8>




![png](index_files/index_28_1.png)


You can see that the ACF here seems a little more *stable*, revolving around 0, which is no surprise. Additionally, the autocorrelation for multiples of 12 seems consistently statistically significant, while it decays for longer time lags!

## The Partial Autocorrelation Function

Similarly to the Autocorrelation Function, the **Partial Autocorrelation Function** (or PACF) gives the partial correlation of a time series with its own lagged values, controlling for the values of the time series at all shorter lags. It contrasts with the autocorrelation function, which does not control for other lags. PACF can be thought of as a summary of the relationship between a time series element with observations at a lag, *with the relationships of intervening observations removed*.

Let's plot the partial autocorrelation function of our "Diet" series. There is no Partial correlation function option in Pandas, but luckily, `Statsmodels` has one in its `tsaplots` module!


```python
from statsmodels.graphics.tsaplots import plot_pacf
from matplotlib.pylab import rcParams

rcParams['figure.figsize'] = 14, 5

plot_pacf(diet, lags = 100);
```


![png](index_files/index_30_0.png)


The partial autocorrelation function can be interpreted as a regression of the series against its past lags. It helps you come up with a possible order for the auto regressive term. The terms can be interpreted the same way as a standard linear regression, that is the contribution of a change in that particular lag while holding others constant. The use of PACF will become more clear when we will be looking at some more "advanced" time series next!

Sidenote: There is also a function `plot_acf` in statsmodels, which serves as an alternative to Pandas' `autocorrelation_plot`:


```python
from statsmodels.graphics.tsaplots import plot_acf
from matplotlib.pylab import rcParams

rcParams['figure.figsize'] = 14, 5

plot_acf(diet, lags = 100);
```


![png](index_files/index_32_0.png)


Note that the plots (and especially the confidence bands) are slightly different. Feel free to have a loot at [this stackoverflow post](https://stackoverflow.com/questions/36038927/whats-the-difference-between-pandas-acf-and-statsmodel-acf) if you want to dig deeper.

## Addional reading

[This blogpost](https://machinelearningmastery.com/gentle-introduction-autocorrelation-partial-autocorrelation/) gives a great overview on what you've seen in this lesson! We'll learn about autoregression and moving average models later, so don't worry about this section too much yet!

## Summary

Great, you've now been introduced to correlation, the ACF and PACF. Let's practice in the next lab!
