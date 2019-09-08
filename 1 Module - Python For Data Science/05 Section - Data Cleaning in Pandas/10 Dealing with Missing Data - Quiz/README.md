# Dealing with Missing Data - Quiz

## Introduction

This quiz is to check your understanding for strategies we've covered for detecting and dealing with missing data.

???

<h1>Missing Data Quiz</h1>

?: Which of the following is a problem that missing data could cause?

( ) Some visualizations will not work with missing data
(X) Some types of data cleaning steps won't work with null values
( ) Machine learning models will break when they encounter null values
( ) All of the above

?: How does pandas represent missing values when displaying a DataFrame or Series object?

(X)
```python
  NaN
```
( )
```python
Null
```
( )
```python
None
```
( )
```python
"Missing Value"
```

?: What will the following code snippet return?

```python
some_dataframe.isna()
```

( ) A count of the missing values in each column
( ) A count of the missing values in each row
( ) A single boolean value `True` if the DataFrame contains one or more missing values, or `False` if there are none.  
(X) A corresponding dataframe of boolean values, with `True` in cells that contain missing values, and `False` in cells that contain valid data

?: Which of the following code snippets returns a count of the missing values in each column of a DataFrame?

(X) `some_dataframe.isna().sum()`
( ) `some_dataframe.dropna()`
( ) `some_dataframe.is_na().sum()`
( ) `some_dataframe.value_counts.is_na()`

?:  Select all the correct code snippets that return the unique values for a given column.

[ ] `some_dataframe.get_unique_values()`
[ ] `some_dataframe.unique()`
[X] `some_dataframe['some_column'].unique()`
[X] `some_dataframe.some_column.unique()`

?: You're cleaning up a DataFrame with ~1000 observations.  You notice that one categorical column contains 512 missing values. What strategy should you employ to deal with these missing values?

( ) Drop all rows with missing values
(X) Drop the column entirely
( ) Replace all missing values with the column mean
( ) Replace all missing values with randomly sampled values from this column

?: True or False: `some_dataframe.dropna()` will drop all rows containing 2 or more missing values.

( ) True
(X) False

?:  Select all valid strategies for dealing with null values in a column containing numerical data, assuming that we can't afford to lose any data.  

[X] Replace missing values with the column median
[ ] Replace missing values with the column mode
[X] Convert the column to categorical format using Coarse Classification ('Binning')
[ ] Leave the Null values as is


???
