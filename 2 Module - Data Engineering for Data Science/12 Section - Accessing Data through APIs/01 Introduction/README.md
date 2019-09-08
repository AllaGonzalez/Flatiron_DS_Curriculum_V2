
# Introduction

## Introduction
In this section, you'll be learning about APIs and why they'll be important to you as a data scientist.

## Objectives
You will be able to:
* Understand and explain what is covered in this section
* Understand and explain why the section will help you to become a data scientist

## APIs

One of the many ways you'll find yourself accessing data as a professional data scientist is via APIs (Application Programming Interfaces). Typically you'll send a request and get some data back - often in JSON or XML format. In this section you'll get some hands on experience retrieving and working with data provided by a range of different APIs.

### Introduction to APIs

We start off the section by providing a conceptual introduction to various kinds of APIs and some of the reasons that businesses create them.

### The Client Server Model

We then look at the basic model of "clients" and "servers" to provide a framework for thinking about how your "client" retrieves information from an API "server".

### The Request/Response Cycle

Next we look at the fundamental mechanism by which web based APIs are typically accessed - sending a HTTP request and then processing the response provided by the server. We also get a little experience of working with http requests using the Python `.get()` method within the Requests package. We also get some hands on experience retrieving information from NASA using [Open Notify](http://open-notify.org/).


### APIs and OAuth

Usually, access to a given API is limited to avoid abuse. One of the most common mechanisms for identifying your API requests to make sure they fit within acceptable usage guidelines is OAuth - Open Authorization - a standard for authorizing clients across web requests. In this section we provide an overview of what OAuth is and how it works by looking at how it is implemented by Dropbox.

### Working with the Yelp API

Next we get some practice working with a real API, retrieving information from the Yelp API.

### Building a GIS with Yelp and Folium

Finally, we wrap up the section by building out a Geographical Information System using data from Yelp and Folium to display it on a map.


## Summary

Many companies provide access to their data via an API, so being able to connect to and work with data provided via an API is a critical skill as a professional data scientist.
