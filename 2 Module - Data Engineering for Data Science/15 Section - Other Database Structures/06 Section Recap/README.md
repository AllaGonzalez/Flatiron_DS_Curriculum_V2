
# NoSQL Section Recap

## Introduction

In this lesson, we'll review the major concepts we've learned in this section. 

## NoSQL vs. SQL

We began this lesson by comparing and contrasting Relational Databases/SQL with the various NoSQL database options that are out there, and outlined examples for when we would want to use each. 

The 4 different kinds of NoSQL Databases are:

* Document Stores
* Key-Value Stores
* Column Stores
* Graph Databases

### RDDs and Hadoop/Spark

We also took some time to dig into another data storage paradigm, **_Resilient Distributed Datasets_**, or **_RDDs_** such as Spark and Hadoop. We explored how these databases uses redundancy to ensure that data is **_Fault Tolerant_**, and examined how the driving idea behind these paradigms , **_MapReduce_**, gives us great speed ups when working with truly massive datasets in 
a distributed manner. 


## MongoDB

Next, we explored how to install **_MongoDB_** and get the **_MongoDB Server_** up and running. We learned some commands that we could use to interact with mongo right there in the server shell, and then focused on connecting to our MongoDB server with Python. 

You should remember the following high-level takeaways from MongoDB:

* You use the `pymongo` library and a little boilerplate to connect to the MongoDB Database.
* In MongoDB, records are referred to as **_Documents_**.
* We can create groups of documents called **_Collections_**.
* Records are inserted by assing in our data as Python Dictionaries. 
    * We can insert a single record with our collection object's `insert_one()` method.
    * We can insert many records by creating a list of dictionaries and passing the entire list to the collection object's `'insert_many()'` method. 
* We can write queries by using the collection object's `'find()'` method. 
* We can **_filter_** our queries by passing in the key-value pairs to filter by.
* We can also use logic on our filters by making use of **_modifiers_**.

## Summary

In this lesson, we reviewed all the major concepts we covered in this section. 
