
# Section Recap

## Introduction

In this section, you learned about time series modeling! Let's review some of the specific things you have learned.

## Objectives
You will be able to:
* Understand and explain what was covered in this section
* Understand and explain why this section will help you become a data scientist

## Key Takeaways

The key takeaways from this section include:
* A White Noise model has a fixed and constant mean and variance, and no correlation over time
* A Random Walk model has no specified mean or variance, but has a strong dependence over time
* The Pandas `corr()` function can be used to return the correlation between various time series data sets
* Autocorrelation allows us to identify how strongly each time series observation is related to previous observations
*  The autocorrelation function (ACF) is a function that represents autocorrelation of a time series as a function of the time lag
* The Partial Autocorrelation Function (or PACF) gives the partial correlation of a time series with its own lagged values, controlling for the values of the time series at all shorter lags
* ARMA (AutoRegressive and Moving Average) modeling is a tool for forecasting time series values by regressing the variable on its own lagged (past) values
* ARMA models assume that you've already detrended your data and that there is no seasonality
* ARIMA (Integrated ARMA) models allow for detrending as part of the modeling process and work well for data sets with trends but no seasonality
* SARIMA (Seasonal ARIMA) models allow for both detrending and seasonality as part of the modeling process
* Fracebook Prophet enables data analysts and developers alike to perform forecasting at scale in Python
* Prophet uses Additive Synthesis for time series forecasting


