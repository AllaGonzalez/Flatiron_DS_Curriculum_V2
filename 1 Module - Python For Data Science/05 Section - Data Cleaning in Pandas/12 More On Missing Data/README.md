
# More On Missing Data

## Introduction

Now that you've seen various methods of how to deal with missing data, its time to further discuss how to choose and appropriate methodology given a particular scenario. Commonly, many people will immediately turn to imputing the mean or median of a feature with missing values. This can be valid and effective methodology, hence why it is standard, but does have caveats. For example, doing so will reduce the overall variance of your dataset which should be taken into account when performing subsequent analyses or training a machine learning algorithm on the data set.

## Objectives

You will be able to: 

* Consider the impacts of various techniques for dealing with missing data.
* Check a dataset for duplicates
* Uncover missing values that are not null


```python
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
```


```python
df = pd.read_csv('titanic.csv')
df.head()
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
      <th>Unnamed: 0</th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>A/5 21171</td>
      <td>7.2500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>PC 17599</td>
      <td>71.2833</td>
      <td>C85</td>
      <td>C</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>STON/O2. 3101282</td>
      <td>7.9250</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>113803</td>
      <td>53.1000</td>
      <td>C123</td>
      <td>S</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>5</td>
      <td>0</td>
      <td>3</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>373450</td>
      <td>8.0500</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.plotting.scatter_matrix(df, figsize=(10,10));
```


![png](index_files/index_3_0.png)


## Checking for Missing Data

Typically, the first step in checking for missing data is to simply use the df.info() method. This gives us various information about the columns including their data type and the number of non-null values.


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 891 entries, 0 to 890
    Data columns (total 13 columns):
    Unnamed: 0     891 non-null int64
    PassengerId    891 non-null int64
    Survived       891 non-null int64
    Pclass         891 non-null object
    Name           891 non-null object
    Sex            891 non-null object
    Age            714 non-null float64
    SibSp          891 non-null int64
    Parch          891 non-null int64
    Ticket         891 non-null object
    Fare           891 non-null float64
    Cabin          204 non-null object
    Embarked       889 non-null object
    dtypes: float64(2), int64(5), object(6)
    memory usage: 90.6+ KB


As you can see, Age and Cabin have a substantial amount of missing values, and Embarked has 2 extraneous missing values.

## Checking for Duplicates

While `df.info()` is a good initial spot check for missing values, it may not catch more subtle anomalies in the data such as duplicates. While these values are populated, it is always worrisome if we have observation rows with identical data.


```python
duplicates = df[df.duplicated()]
print(len(duplicates))
duplicates.head()
```

    100





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
      <th>Unnamed: 0</th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>A/5 21171</td>
      <td>7.25</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>A/5 21171</td>
      <td>7.25</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>A/5 21171</td>
      <td>7.25</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>A/5 21171</td>
      <td>7.25</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>3</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>A/5 21171</td>
      <td>7.25</td>
      <td>NaN</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>



Similarly, if a feature such as PassengerId can be assumed to be unique, we can further check if there are duplicate rows based on a subset of the DataFrame columns.


```python
duplicates = df[df.duplicated(subset='PassengerId')]
print(len(duplicates))
duplicates.tail()
```

    500





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
      <th>Unnamed: 0</th>
      <th>PassengerId</th>
      <th>Survived</th>
      <th>Pclass</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
      <th>SibSp</th>
      <th>Parch</th>
      <th>Ticket</th>
      <th>Fare</th>
      <th>Cabin</th>
      <th>Embarked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>395</th>
      <td>257.0</td>
      <td>839.0</td>
      <td>0.0</td>
      <td>?</td>
      <td>Rush, Mr. Alfred George John</td>
      <td>male</td>
      <td>47.0</td>
      <td>0.0</td>
      <td>4.0</td>
      <td>113510</td>
      <td>12.8750</td>
      <td>B79</td>
      <td>C</td>
    </tr>
    <tr>
      <th>396</th>
      <td>300.0</td>
      <td>839.0</td>
      <td>1.0</td>
      <td>2</td>
      <td>Skoog, Master. Harald</td>
      <td>female</td>
      <td>17.0</td>
      <td>5.0</td>
      <td>5.0</td>
      <td>2671</td>
      <td>17.4000</td>
      <td>E49</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>397</th>
      <td>65.0</td>
      <td>839.0</td>
      <td>0.0</td>
      <td>?</td>
      <td>Slocovski, Mr. Selman Francis</td>
      <td>male</td>
      <td>47.0</td>
      <td>8.0</td>
      <td>4.0</td>
      <td>239854</td>
      <td>7.0500</td>
      <td>B49</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>398</th>
      <td>807.0</td>
      <td>839.0</td>
      <td>1.0</td>
      <td>?</td>
      <td>Glynn, Miss. Mary Agatha</td>
      <td>male</td>
      <td>48.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>36866</td>
      <td>8.6625</td>
      <td>F G63</td>
      <td>C</td>
    </tr>
    <tr>
      <th>399</th>
      <td>664.0</td>
      <td>839.0</td>
      <td>0.0</td>
      <td>?</td>
      <td>Sobey, Mr. Samuel James Hayden</td>
      <td>male</td>
      <td>14.5</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>2672</td>
      <td>108.9000</td>
      <td>C148</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>



## Checking for extraneous values

Sometimes, null values are even further hidden within a dataset. For example, sometimes an entry such as `999999` is used for missing values, or an arbitrary date such as `12-01-1970` might be set for unknown dates. In general, doing a quick eyeball and previewing the top occurring values for each feature can help further tease out peculiarities in the data set.


```python
for col in df.columns:
    print(col, '\n', df[col].value_counts(normalize=True).head(), '\n\n')
```

    Unnamed: 0 
     0.0      0.073329
    680.0    0.003595
    816.0    0.003595
    2.0      0.002876
    420.0    0.002876
    Name: Unnamed: 0, dtype: float64 
    
    
    PassengerId 
     839.0    0.288282
    1.0      0.072610
    881.0    0.000719
    757.0    0.000719
    195.0    0.000719
    Name: PassengerId, dtype: float64 
    
    
    Survived 
     0.0    0.618979
    1.0    0.381021
    Name: Survived, dtype: float64 
    
    
    Pclass 
     3    0.475198
    1    0.219267
    2    0.199137
    ?    0.106398
    Name: Pclass, dtype: float64 
    
    
    Name 
     Braund, Mr. Owen Harris                      0.072610
    Stone, Mrs. George Nelson (Martha Evelyn)    0.003595
    Maioni, Miss. Roberta                        0.002876
    Chapman, Mr. John Henry                      0.002876
    Butler, Mr. Reginald Fenton                  0.002876
    Name: Name, dtype: float64 
    
    
    Sex 
     male      0.641265
    female    0.358735
    Name: Sex, dtype: float64 
    
    
    Age 
     22.0    0.106700
    18.0    0.029777
    24.0    0.029777
    25.0    0.023987
    30.0    0.023160
    Name: Age, dtype: float64 
    
    
    SibSp 
     0.0    0.473041
    1.0    0.263120
    2.0    0.060388
    3.0    0.057513
    8.0    0.055356
    Name: SibSp, dtype: float64 
    
    
    Parch 
     0.0    0.595255
    1.0    0.125090
    2.0    0.099209
    4.0    0.051042
    5.0    0.048167
    Name: Parch, dtype: float64 
    
    
    Ticket 
     A/5 21171    0.072610
    CA 2144      0.005751
    CA. 2343     0.005751
    113781       0.005751
    347082       0.005751
    Name: Ticket, dtype: float64 
    
    
    Fare 
     7.2500     0.082674
    8.0500     0.033070
    13.0000    0.031632
    7.8958     0.029475
    7.7500     0.026600
    Name: Fare, dtype: float64 
    
    
    Cabin 
     A20            0.013289
    B41            0.013289
    E121           0.013289
    C23 C25 C27    0.011628
    C83            0.011628
    Name: Cabin, dtype: float64 
    
    
    Embarked 
     S    0.643910
    C    0.221102
    Q    0.134988
    Name: Embarked, dtype: float64 
    
    


You can see that we've uncovered another case of missing data that did not show up before! The Pclass feature has `?` for roughly 10% of the entries.

## Choosing a Methodology

Now that you have some ideas of various methods for dealing with missing data, how do you choose which to use? The answer will depend on the scenario and specifics to the application itself. As a general rule of thumb, we tend towards imputing values rather than dropping them, as we wish to use as much information as possible. That said, larger gaps where data is missing can pose more substantial problems, and thereby warrant alternative approaches. We'll take a look at specific cases below in more detail, but here's a quick table of your options.

|         | Continuous          | Categorical  |
| ------------- |:-------------:| -----:|
| Delete      | Delete Rows (observations) <br> Delete column (entire variable)| Delete Rows (observations) <br> Delete column (entire variable)|
| Replace | replace using median/mean | replace using mode
| Keep | keep as NA (not possible for many ML algorithms) | NA category

## Imputing Values

Imputing values is often a go to option when dealing with missing data. For example, if we are building a machine learning model with the data, many algorithms cannot handle missing values. By imputing data, we still get to use the full extent of the data at hand without having to throw away data, which, as you know, is an easy option.


```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 1391 entries, 0 to 399
    Data columns (total 13 columns):
    Unnamed: 0     1391 non-null float64
    PassengerId    1391 non-null float64
    Survived       1391 non-null float64
    Pclass         1391 non-null object
    Name           1391 non-null object
    Sex            1391 non-null object
    Age            1209 non-null float64
    SibSp          1391 non-null float64
    Parch          1391 non-null float64
    Ticket         1391 non-null object
    Fare           1391 non-null float64
    Cabin          602 non-null object
    Embarked       1289 non-null object
    dtypes: float64(7), object(6)
    memory usage: 152.1+ KB


## Considerations When Imputing

When imputing missing values, keep in mind that you are influencing the distribution of this variable. For example, if you impute the mean, you will reduce the variance of that feature. 

## When to Drop Rows


Dropping rows is an appropriate choice if there are very few missing values to start with. After all, we do not wish to throw away troves of data if we have it, so cases in which there are larger occurrences of missing values, dropping all occurrences is typically inadvisable.

## When to Drop Columns

Dropping columns is typically a last case resort. That said, if a feature does not add predictive value to the machine learning algorithm driving your application, dropping said feature has no cost.

A few simple lines such as this can easily subset your DataFrame:  
~~~
cols_to_remove = ['col1', 'col2']
cols = [col for col in df.columns if col not in cols_to_remove]
subset = df[cols]
~~~

## Summary

In this lesson, we took a look at methods for identifying duplicate data as well as missing data that is not null, but filled with a placeholder value (such as ?). We also began to discuss considerations when dealing with missing data, which you yourself will further grapple with in the upcoming lab.
