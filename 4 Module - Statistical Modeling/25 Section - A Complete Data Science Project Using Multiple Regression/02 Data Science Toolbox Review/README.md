
# Data Science Toolbox Review

## Introduction 

In this lesson, you'll get a chance to review some of the many skills you've learned to date! You've developed a range of skills to date from general programming skills and OOP to databases, data analysis and statistics! Hopefully you're excited to pull all of these pieces together and conduct a full data-science investigation from ingestion to modeling! With that, here's a quick review of some of the most pertinent skills you'll be using along the way!

## Objectives

You will be able to:

* Perform SQL select statements including using joins
* Summarize pandas methods for high level exploratory data analysis
* Outline a Regression Modeling Process

## SQL

You've seen how SQL, Structured Query Language, is a wonderful method for organizing data. Having data in a database allows multiple users to access, query and update shared data simultaneously. As such, many companies store their data in databases, and SQL is undoubtedly the most popular implementation. You saw that most statements began with the ```
select ``` clause, and from there you specify which columns you wish to select, the table from which you wish to select them, and appropriate filters using the ```where``` clause. You can also aggregate data with the `group by` clause, and apply further filters to those roll-ups using the ```having``` clause. Furthermore, you can select data from multiple tables using a ``join``, so long as the two tables have a common key(s) which you specify with the `using` clause, if the column names are identical, or more verbosely, you can specify how to join the tables with the `on` clause. 

For example, here's the schema for the mock customer relationship database that you've seen before: 


<img src='images/Database-Schema.png' width=550>

If you wanted to select some aggregate statistics regarding employees and customers on a per office basis for cities with at least 2 offices, you could write a query like this:  

```SQL
select officeCode,
       city,
       count(employeeNumber) as num_employees,
       count(customerNumber) as num_customers,
       sum(amount) as total_payments_received
       from offices
       join employees
       using(officeCode)
       join customers
       on employeeNumber = salesRepEmployeeNumber
       join payments
       using(customerNumber)
       group by 1,2
       where city in (select city from offices group by 1 having count(*)>1);
```

Look at that; you even got to see the use of a subquery once again!
       

## Data Exploration and Visualization

Once you've loaded in some data from a SQL database or elsewhere, its generally time to start investigating and cleaning up that data. Remember that pandas comes with many useful methods for quickly exploring your dataset. For example, you may want to initially check the datatypes of your dataset and how many null values exist for each of the various features. This is incredibly easy using the `df.info()` method. Similarly, if you want to generate aggregate statistics, you can simply call the `.describe()` method on a DataFrame as in `df.describe()`. If you want to quickly explore the distribution and pairwise correlations between your features, then using the `pd.plotting.scatter_matrix(df)` method will quickly display a grid of histograms and scatter plots for the various features; the diagonal entries are the distributions for each of the variables, while any other cell [i,j] is a scatter plot of feature i vs feature j.  

Recall that when initially exploring your data, you are both looking for insights and anomalies. Typically, you want to get familiar with the data, what it represents, and how it is represented. This will often give you further ideas about how to mine the data for structure and answer questions regarding the application.

## Regression

After acquiring and exploring your data (including cleaning it up), you'll then go on to model said data using the regression techniques you learned about earlier. With this, recall that there are four main assumption underlying a linear regression model.

### 1. Linearity

With linear models, the target variable is being modeled as a linear combination of the independent variables. As such, there should be a linear relationship between the target variable and the various features being used. If the rate of change between the target variable and one of the features is non-linear and displays other characteristics such as an exponential acceleration, then prior transformations of the data are necessary before applying a regression model. 


### 2. Normality

With linear models, the errors from the model are assumed to be normally distributed. A good heuristic to initially check for this is to use a Q-Q plot. 

### 3. Homoscedasticity

Along with the assumption of normally distributed, error terms should also not be correlated with the target variable or other features within the model. If errors indeed appear to be random and there are no discernible trends, then the errors are said to be homoscedastic. Looking at a simple residual plot against the target variable or other feature is generally sufficient to gauge this.

### 4. Independence

Finally, regression models assume that the various independent features feeding into the model are independent. You'll take a further look at this in this section and investigate how to check for multicollinearity. Multicollinearity is when a variable can be predicted with substantial accuracy by a separate set of features. Previously, you've examined to two variable case: it's unwise to include two features in a regression model that are highly correlated. Similarly, in a multivariate case, having a set of features that can effectively predict another independent feature can be problematic. Such phenomenon will not reduce the overall accuracy of the model, but will severely impede interpretation as coefficient weight of the model become unstable so it is difficult or impossible to determine which features are most influential.


## Summary

In this lesson, you took a quick review of SQL, Data exploration and regression models. If you are looking for a more substantial review, feel free to turn back to some of the previous material. With that, it's time to take a look at some general frameworks for data science workflows!
