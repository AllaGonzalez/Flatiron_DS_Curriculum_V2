
# SQL Database Data Types

## Introduction
In this lesson, you'll cover the importance of specifying datatypes, and the different types of data you can store in a SQLite database.

## Objectives

You will be able to:

- Describe data typing and how it allows for operations to be performed with predictable results
- List four different types of data you can store in a SQLite database
- Define three specific SQLite database types: Text, Integer, and Real

## Why Do Data Types Matter?

You've seen that when you create a table, you need to include a name for it as well as define at least one column. You define columns in a `CREATE` statement by including a name and a datatype to let SQLite know the kind of data you will be storing there. The practice of explicitly declaring a type is known as "typing." 

Why is it important that you use typing in our database? Simply put, typing allows us to exercise some level of control over our data. Typing not only informs our database of the kind of data you plan to store in a column but it also restricts it. For instance, look at the age column below in our cats table. What do you mean by age? What if you had this:

| name  |  breed  |  age  |
|-------|---------|-------|
| Maru  |  Scottish Fold |   3   |
| Hannah |  Tabby  |  two  |
| Lil' Bub |  American Shorthair  |  5.5  |

Did you intend age to be represented as a whole-number, a word, or a decimal? If you were asked to add up the ages of all the cats you could simply convert the 'two' to 2 in your head, but your database can't do that. It doesn't have that ability because the logic involved in converting a word into a number would be dense and inefficient. What about different languages? What about different spellings? Capitalization, typos, or different hyphenation conventions? These are just some reasons this might start to get crazy. In other words, because databases are designed to store large amounts of data, they are very concerned with storing, accessing, and acting upon that data as efficiently and normally as possible.

Typing gives us the ability to perform all kinds of operations with predictable results. For instance, the ability to perform math operations like `SUM` - i.e. summing integers - doesn't just depend on everything being an integer of some sort but would also expect it. If you tried, for example,  to `SUM` all of the cats in the above table, SQLite would actually attempt to convert, or cast, their type to something it can `SUM`. It would try to convert anything it can to an `INTEGER` and ignore alpha characters. This can lead to real problems. Without typing, our data might get complicated and messy, and it would be difficult to ask the database questions about large sets of data.

Simply put, it's important to adhere strictly to only storing data that fits with the datatype you have given to a particular column.

## Datatypes

Different database systems also have different datatypes available, which are important and useful to know whenever you are dealing with those systems. SQLite is a good starting point to learn about datatypes because it only has four basic categories of datatypes; they are:

```SQL
TEXT
INTEGER
REAL
BLOB
```
Let's explore each category in more detail.

### TEXT

Any alphanumeric characters which you want to represent as plain text. The body of this paragraph is text. Your name is text. Your email address is a piece of text. Your height, weight, and age, however, are probably not.

### INTEGER

Anything you want to represent as a whole number. If it's a number and contains no letter or special characters or decimal points then you should store it as an integer. If you use it to perform math or create a comparison between two different rows in our database, then you definitely want to store it as an integer. If it's just a number, it's generally not a bad idea to store it as an integer. You might never add two house address numbers together, but you might want to sort them numerically. For example in the preceding case, you might want to get the biggest number and not the longest piece of text.

### REAL

Anything that's a plain old decimal like 1.3 or 2.25. SQLite will store decimals up to 15 characters long. You can store 1.2345678912345 or 1234.5678912345, but 1.23456789123456789 would only store 1.2345678912345. In other database systems this is called 'double precision.'

With these three types in hand, you are going to be able to work our way through the next several topics, and this whole typing concept is going to quickly become second nature for you.

### BLOB

You may encounter the `BLOB` datatype while you're Googling or doing any further reading on SQLite. For now, you will not use `BLOB`. It is generally used for holding binary data.

##Bonus: Note on SQLite
To increase its compatibility with other database engines (E.G. mySQL or PostgreSQL), SQLite allows the programmer to use other common datatypes outside of the four mentioned above. This is why you are referring to `TEXT INTEGER REAL BLOB` as datatype "categories". All other common datatypes are lumped into one of the four existing datatypes recognized by SQLite. 

For example, `INT` is a common datatype used outside of SQLite. SQLite won't complain if you define a column as an `INT` datatype. It will simply lump it into the `INTEGER` category and store it as such.

To accommodate this, SQLite has a pretty complicated system of categorizing datatypes that involves `Storage Classes`, `Type Affinities`, and `Datatypes`. For a deeper dive, check out the 
[SQLite3 Documentation on Datatypes](http://www.sqlite.org/datatype3.html)

## Summary
Great! Now that you've finished this lesson you know why it is important to specify datatypes, and you know about the different types of data you can store in a SQLite database.

