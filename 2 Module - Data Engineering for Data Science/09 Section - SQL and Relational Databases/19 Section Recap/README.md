
# Section Recap

## Introduction

In this section, you learned about making different SELECT queries in SQL.

## Objectives

You will be able to:
* Understand and explain what was covered in this section
* Understand and explain why this section will help you become a data scientist

## SELECT

The first part that you saw with sql is how to select data from tables. You saw how to connect to a database and query basic data from a table using column names or the wildcard parameter `*`. 

## Filters

After looking at basic select statements, you then saw how to filter your selections using the `where` clause.

## Ordering

Along with filtering, you also saw how to order your query selections. To do this, you use the `order by` clause. Remember that the default behavior there is to return results in ascending order. You can verbosely specify this with the `asc` keyword, or modify the behavior to sort in descending order with the `desc` keyword.

## Grouping

Next up, you saw you to create aggregates with your data. This involved using the `group by` statement. You saw that you can both explicitly state the column names that you wish to group by or that you can use aliases for the columns using numbers such as 1,2,3. You also got to investigate some aggregate functions such as `count()`, `max()`, `min()`, and `avg()`. Finally, you also saw that you can filter based on the results of aggregate functions using the `having` clause. 

## Joins

After taking a look at more complex queries for a single table, you started to investigate how you could combine data from multiple tables. You did this using the `join` clause. Remember that you can specify the links between tables with the `using()` clause if the column name is identical between the tables or the `on` clause if you must specify the link more manually. You also saw how to alias table names during your joins.

## Subqueries

With some of the more complicated join and aggregate scenarios that began to arise, you also saw how to use subqueries to break down complex queries into parts. You also saw how you could potentially create aggregates of aggregates using subqueries.

## Database Administration

Wrapping up the section, you saw how to create databases, tables and subsequently populate those containers with data. You also saw how to delete or modify information. Database administration is a complex topic that has a lot more considerations including user permissions and improving query execution time, but this was a solid introduction to get you up and running.

## Summary

Congratulations! You should have a good amount of SQL skills to harness in your data adventures going forward! While you are apt to use other tools such as pandas to do a lot of your exploratory analysis and data manipulation, databases provide a much more powerful data storage option then flat files like csv or excel workbooks.
