
# Filtering and Ordering

## Introduction

In this lesson, you'll continue to see how to write SQL queries for retrieving and adding specific data to SQL database tables.

## Objectives
You will be able to:
* Limit the number of records returned by a query using `LIMIT`
* Filter results using `BETWEEN` and `IS NULL`
* Order the results of your queries by using `ORDER BY` (`ASC` & `DESC`)


## What is a SQL Query?

The term "query" refers to any SQL statement that retrieves data from your database. In fact, you've already written a number of SQL queries using basic `SELECT` statements. You've already seen how to retrieve single units of data, or rows, with queries like these:

To select all of the rows from a `cats` table:

```sql
SELECT * FROM cats;
```

To select only rows representing data meeting certain conditions:

```sql
SELECT * FROM cats WHERE name = "Maru";
```

However, what if you wanted to select the oldest cat? Or all of the cats that don't currently belong to an owner? Or all of the cats with short names?

Data storage isn't very useful if you can't manipulate, view, and analyze that data. Luckily for us, SQL is actually a powerful tool for doing just that.

In this exercise, you'll walk through executing a handful of common and handy SQL queries.

## Code Along: SQL Queries

The cats table is populated with the following data:


|id  |name     |age    |breed              |owner_id|
|----|---------|-------|-------------------|-----------|
|1   |Maru     |3.0    |Scottish Fold      |1.0        |
|2   |Hana     |1.0    |Tabby              |1.0        |
|3   |Lil' Bub |5.0    |American Shorthair |NaN        |
|4   |Moe      |10.0   |Tabby              |NaN        |
|5   |Patches  |2.0    |Calico             |NaN        |
|6   |None     |NaN    |Tabby              |NaN        |

### Creating our Database

In this code along, you'll start by connecting to `pets_database.db`.

Recall that you can do this by running the following commands:

```python
import sqlite3 
conn = sqlite3.connect('pets_database.db')
cur = conn.cursor()
```


```python
# create database connection here
```

**Let's check out our `cats` table with an SQL query:**

```python
cur.execute('''SELECT * FROM cats;''').fetchall()
```

> **Note:** the method `.fetchall()` returns a `list` where each record is represented as a `tuple`, which you can think of as a `list`-like object. If you would like to retrieve an element from a `tuple`, you simply access it by-index -- similar to how you access the elements of a normal Python list. (i.e. `example_tuple[0]` - returns element at index `0`)


```python
# select all data from cats data here
```

This should return:

```python
[(1, 'Maru', 3, 'Scottish Fold', 1),
 (2, 'Hana', 1, 'Tabby', 1),
 (3, "Lil' Bub", 5, 'American Shorthair', None),
 (4, 'Moe', 10, 'Tabby', None),
 (5, 'Patches', 2, 'Calico', None),
 (6, None, None, 'Tabby', None)]
```

### `ORDER BY`

The first query modifier you'll explore is `ORDER BY`. This modifier allows us to order the table rows returned by a certain `SELECT` statement. Here's a boilerplate `SELECT` statement that uses `ORDER BY`:

```python
cur.execute('''SELECT column_name FROM table_name ORDER BY column_name ASC|DESC;''').fetchall()
```

**Let's select our cats and order them by age:**

```python
cur.execute('''SELECT * FROM cats ORDER BY age;''').fetchall()
```


```python
# select all cats order by age here
```

This should return the following:

```python
[(6, None, None, 'Tabby', None),
 (2, 'Hana', 1, 'Tabby', 1),
 (5, 'Patches', 2, 'Calico', None),
 (1, 'Maru', 3, 'Scottish Fold', 1),
 (3, "Lil' Bub", 5, 'American Shorthair', None),
 (4, 'Moe', 10, 'Tabby', None)]            
```

When using `ORDER BY`, the default is to order in ascending order. If you want to specify though, you can use `ASC` for "ascending" or `DESC` for "descending." **Let's try to select all of our cats and sort them by age in descending order.**

```python
cur.execute('''SELECT * FROM cats ORDER BY age DESC;''').fetchall()
```


```python
# select cats order by age descending here
```

This should return

```python
[(4, 'Moe', 10, 'Tabby', None),
 (3, "Lil' Bub", 5, 'American Shorthair', None),
 (1, 'Maru', 3, 'Scottish Fold', 1),
 (5, 'Patches', 2, 'Calico', None),
 (2, 'Hana', 1, 'Tabby', 1),
 (6, None, None, 'Tabby', None)]      
```

### `LIMIT`

What if you want the oldest cat? If you want to select extremes from a database table––for example, the employee with the highest paycheck or the patient with the most recent appointment––we can use `ORDER BY` in conjunction with `LIMIT`.

`LIMIT` is used to determine the number of records you want to return from a dataset. For example:

```sql
SELECT * FROM cats ORDER BY age DESC LIMIT 1;
```

> **Note:** When you would only like the first result (or one result as is the case in the example above) you can use the sqlite3 method `.fetchone()` which, instead of returning a list of results, returns the first result (or the record at index 0). you can use this in place of or in conjunction with `LIMIT 1` in order to get back a single element.


```python
cur.execute('''SELECT * FROM cats ORDER BY age DESC LIMIT 1;''').fetchone() 

## This returns the same element as the above:
# cur.execute('''SELECT * FROM cats ORDER BY age DESC;''').fetchone()
```

This part of the statement: `SELECT * FROM cats ORDER BY age DESC` returns all of the cats in order from oldest to youngest. Setting a `LIMIT` of `1` returns just the first, i.e. oldest, cat on the list.

After you execute the above statement you should see:

```python
(4, 'Moe', 10, 'Tabby', None)            
```
**Let's get the two oldest cats:**

```sql
SELECT * FROM cats ORDER BY age DESC LIMIT 2;
```


```python
# select the two oldest cats here
```

Execute that statement and you should see:

```python
[(4, 'Moe', 10, 'Tabby', None), (3, "Lil' Bub", 5, 'American Shorthair', None)]          
```

### `BETWEEN`

As we've already established, being able to sort and select specific data sets is important. Continuing on with our example, let's say you urgently need to select all of the cats whose age is between 1 and 3. To create such a query, you can use `BETWEEN`. Here's a boilerplate `SELECT` statement using `BETWEEN`:

```sql
SELECT column_name(s) FROM table_name WHERE column_name BETWEEN value1 AND value2;
```

**Let's try it out on our `cats` table:**

```sql
SELECT name FROM cats WHERE age BETWEEN 1 AND 3;
```


```python
# find all records between ages 1 and three here
```

This should return:

```python
[('Maru',), ('Hana',), ('Patches',)]
```

### `NULL`

Some cats were added to the Database that weren't given a name. **Let's find them with:**

```sql
SELECT * FROM cats WHERE Name IS null;
```


```python
# select cats where the name field is null here
```

This should return the following:

```python
[(6, None, None, 'Tabby', None)]
```

### `COUNT`

Now, let's talk about the SQL aggregate function `COUNT`.

**SQL aggregate functions** are SQL statements that can get the average of a column's values, retrieve minimum and maximum values from a column, sum values in a column, or count a number of records that meet certain conditions. You can learn more about these SQL aggregators [here](http://www.sqlclauses.com/sql+aggregate+functions) and [here](http://zetcode.com/db/sqlite/select/).

For now, we'll just focus on `COUNT`, which counts the number of records that meet a certain condition. Here's a standard SQL query using `COUNT`:

```sql
SELECT COUNT([column name]) FROM [table name] WHERE [column name] = [value]
```
**Let's try it out and count the number of cats who have an `owner_id` of `1`:**

```sql
SELECT COUNT(owner_id) FROM cats WHERE owner_id = 1;
```


```python
# retrieve the count of cats whose owner id = 1 here
```

This should return:

```python
(2,)
```

### `GROUP BY`

Lastly, we'll talk about the handy aggregate function `GROUP BY`. Like its name
suggests, it groups your results by a given column.

Let's take our table of cats

```bash
id          name        age         breed          owner_id  
----------  ----------  ----------  -------------  ----------
1           Maru        3           Scottish Fold  1         
2           Hana        1           Tabby          1         
3           Lil\' Bub   5           American Shor            
4           Moe         10          Tabby                    
5           Patches     2           Calico                   
6                                   Tabby                    
```

Here, you can see at a glance that there are three tabby cats and
one of every other breed — but what if you had a larger database
where you couldn't just tally up the number of cats *grouped by*
breed? That's where — you guessed it! — `GROUP BY` comes in handy.

``` sql
SELECT breed, COUNT(breed) FROM cats GROUP BY breed;
```


```python
# execute above GROUP BY sql statement here
```

This should return

```python
[('American Shorthair', 1), ('Calico', 1), ('Scottish Fold', 1), ('Tabby', 3)]
```

`GROUP BY` is a great function for aggregating results into different
segments — you can even use it on multiple columns!

```sql
SELECT breed, owner_id, COUNT(breed) FROM cats GROUP BY breed, owner_id;
```


```python
# execute above multiple column group by statement here
```

This should return:

```python
[('American Shorthair', None, 1),
 ('Calico', None, 1),
 ('Scottish Fold', 1, 1),
 ('Tabby', None, 2),
 ('Tabby', 1, 1)]
```

### Note on `SELECT`

We are now familiar with this syntax:

```sql
SELECT name FROM cats;
```

However, you may not know that this can be written like this as well:

```sql
SELECT cats.name FROM cats;
```

Both return:

```python
[('Maru',), ('Hana',), ("Lil' Bub",), ('Moe',), ('Patches',), (None,)] 
```

SQLite allows us to explicitly state the `tableName.columnName` you want to select. This is particularly useful when you want data from two different tables.

Imagine you have another table called `dogs` with a column containing all of the dog names:

```sql
CREATE TABLE dogs (
	id INTEGER PRIMARY KEY,
	name TEXT
);
```

```sql
INSERT INTO dogs (name) VALUES ("Clifford");
```


If you want to get the names of all the dogs and cats, you can no longer run a query with just the column name.
`SELECT name FROM cats,dogs;` will return `Error: ambiguous column name: name`.

Instead, you must explicitly follow the `tableName.columnName` syntax.
```sql
SELECT cats.name, dogs.name FROM cats, dogs;
```

You may see this in the future. Don't let it trip you up!

## Summary

In this lesson, you expanded your SQL knowledge by learning how to modify your data using statements like `ORDER BY`. 
Additionally, you learned how to filter and limit your results.
