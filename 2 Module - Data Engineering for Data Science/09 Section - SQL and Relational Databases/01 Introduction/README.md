
# SQL Introduction

## Introduction

In this section, you'll learn about SQL, which stands for Structured Query Language. It has been around since the 1970's and has many different dialects of the language including MySQL, SQLite and PostgreSQL, to name a few. Each of these has particularities such as specific functions or keywords for that specific implementation. All of these, however, have the same basic structures including basic keywords like SELECT, and the same general database architecture.

## Objectives

You will be able to:

* Name some different types of SQL
* Discuss the basic structure of a SQL database
* Understand some basic SQL queries

## The Structure of SQL Databases 

SQL Databases are the root container for data. Databases are a collection of tables. Each table is similar to a csv-file or a spreadsheet within an Excel workbook. That is, tables are two-dimensional objects with specific columns and associated entries organized into rows. To demonstrate, here is an outline of a database structure:

<img src="images/Database-Schema.png" width=700>

In the diagram, each rectangle is a table, with the table name listed at the top. In this case, we have 8 tables: productlines, products, orderdetails, employees, offices, customers, orders, and payments. Below each of the table names, we have a list of the various column names associated with that table. So for example, the productlines table has four columns: productLine, textDescription, htmlDescription and image. 
  
  You may also note that some of these column names are preceded by an asterix (\*). This indicates that this is the **primary key** for the table. A primary key is a unique identifier for a table. That is, there can only be unique values for this column entry. A common example is a user id. For example, in the employees table, the employeeNumber serves as the primary key for the table. This is an important design choice: if instead lastName and firstName were designated as dual primary keys, problems would arise if two employees had the same name. 
  Primary keys also serve as a link between tables in the database. You can see which tables are related to one another via the lines between them. The circles, arrows and tick marks are all more complex categorizations of these relations which you'll learn more about later.

## Connect to SQL Databases

Your initial primary use case of sql will be querying data stored within databases. To do this, you connect to the database with some sort of tool. This could be via python, as you'll see in the next lesson, the command line, or a GUI tool such as SQLWorkbench. Once you're connected to the database, you can then read and select data from the database, or even write data to the database.

## Querying Databases

To retrieve data from one or more tables you usually use a `select` statement. 

A simple query would look something like this:
```SQL
SELECT col1, col2, col3
FROM table
WHERE records match criteria
LIMIT 100;
```

Another similar query to preview all of the columns from the first 5 rows of a table would look like this:  

```SQL
SELECT *
FROM table
LIMIT 5;
```

Notice how all of these statements start with the `SELECT` clause, followed by what you want to select. If selecting multiple columns, you separate them with a comma. Then you specify where that data is being retrieved from the using the `FROM` clause followed by the table name. Afterward, you can provide conditions such as filters or sorting. To demonstrate, here's a more complex example where you could preview the 10 most expensive payments received.

```SQL
SELECT *
FROM payments
ORDER BY amount DESC
LIMIT 10;
```

Notice all the keywords in SQL appear bolded and in green. Although not required, all the code here also has capitalized all of the keywords to make them further stand out.

## Summary

In this lesson, you got a quick overview of what SQL is, and saw a few of your first SQL queries! Remember that there are multiple SQL dialects all with particular anomolies and differences, but the overall language is generally fairly similar and interchangeable.
