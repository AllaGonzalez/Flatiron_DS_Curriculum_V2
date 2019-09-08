
# Introduction

## Introduction
In this section, you will learn about working with an important and ever-present type of data: time series data! Stock market prices, weather, and economic indicators like GDP are a few examples of time series data.

## Objectives
You will be able to:
* Understand and explain what is covered in this section
* Understand and explain why the section will help you to become a data scientist

## Working with Time Series Data

"Time series" data refers to data sets where the progress of time is an important dimension in the data set. For example working with the changes in stock prices, oil flow through a pipeline or even climate data over time requires an understanding of how to work with time series data. In this first of two sections on time series data, we introduce the concept of time series data, look at how to manage and visualize time series data, look at types of trends and how to test for and remove them and then introduce the idea of "time series decomposition". In the next section we'll then introduce techniques for modeling time series data.

### Introduction to Time Series

In this lesson, we start by importing daily minimum temperatures from Melbourne, Australia and  introduce the importance of using dates as index values when importing into Pandas for time series data. We then go through how to downsample and upsample a data set and show some of the built in methods for easily selecting and slicing time series data. We also provide an introduction to some of the most common plots for time series such as a line plot or a dot plot and approaches to grouping and visualizing time series data.

We also introduce the use of time series histograms and density plots for visualizing the distribution of the values without considering the times at which the values were measured, and suggest time series box and whisker plots on a per year basis to get a sense of trends over time. Finally we introduce time series heat maps which can be a great way of getting a sense of how time series data changes across a couple of dimensions (e.g. month to month and year to year).

### Managing Time Series Data Lab

After the (fairly comprehensive) introductory lesson above, it's your chance to get some experience working with time series data. You're going to import some data on atmospheric CO2 levels and get some experience loading the data, slicing it, changing the granularity and performing some basic data cleaning operations on it.

### Visualizing Time Series Data Lab

Next up, working we with the minimum daily temperature from Melbourne again, you'll get a chance to explore the structure of the time series using line plots, understanding and describing the distribution of the observations using histograms and density plots, and measuring the change in distribution over intervals using box and whisker plots and heat map plots.

### Types of Trends

Basic regression tests are often not capable of capturing and predicting time-dependent patterns, so in this lesson we introduce the concept of trends, stationarity and explain the Dickey Fuller Test for performing statistical testing for time series stationarity.

### Testing for Trends Lab

After introducing the concepts in the previous lesson, in this lab you get a chance to implement a number of tests for stationarity of a time series data set.

### Removing Trends

Most time series modeling techniques have a stationarity assumption, so in this lesson we look at some of the techniques available for removing (or reducing) trends and/or seasonality using techniques such as a log transformation, rolling means or differencing.

### Time Series Decomposition

Finally, we end the section by introducing the concept of decomposition - another approach to removing trends and seasonality from a time series data set.


## Summary

This section will provide you with the foundational knowledge for loading and working with time series data, so you'll have the skills required to start to perform time series modeling!

