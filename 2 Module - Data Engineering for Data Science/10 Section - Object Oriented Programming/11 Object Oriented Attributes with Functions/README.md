
# Object Oriented Attributes with Functions

## Introduction
You've been learning a lot about different parts of object-oriented programming; you've seen the purpose of classes, you've seen instance objects, instance variables, and instance methods and how these things all work with each other. In this lab, you'll talk about what a **domain model** is and how it ties into object-oriented programming.

## Objectives

You will be able to:

* Understand the concept of a domain model
* Create a domain model
* Define instance methods that operate on nested data structures

## What Is a Domain Model?

A domain model is the representation of a real-world concept or structure translated into software. This is a key function of object orientation. So far, your Python classes have been used as blueprints or templates for instance objects of that class. As an example, a Driver class would create driver instance objects, and the class would define a basic structure for what that driver instance object should look like and what capabilities it should have. But a class is only one part of a domain model just as, typically, a driver is only one part of a larger structure.

A domain model is meant to mirror that larger, real-world structure. It is more than just one class, it is an entire environment that often depends on other parts or classes to function properly. So, in keeping with a Driver class, you could use the example of a taxi and limousine service as our domain model. There are many more parts to a service like this than drivers alone. Imagine dispatchers, mechanics, accountants, passengers, etc., all being part of the structure of this domain model. In a simplified example, you could have instance and class methods handle things like `dispatch_driver`, `calculate_revenue_from_rides`, `service_taxi`, or any other function of a taxi and limousine service.

As you become more fluent in object-oriented programming and your programs become more complex, you'll see that the other parts of a domain model like passengers, dispatchers, etc., will be classes of their own which interact with each other. 

In this lecture, you'll be using a business as our domain model. With this, you'll continue to see how attributes and methods can be combined to perform operations and store values simultaneously.

## Creating the Class

Here's a simple class template:


```python
class Business():
    def __init__(name=None, biz_type=None, city=None, customers = {}):
        business.name = name
        business.biz_type = biz_type
        business.city = city
        business.customers = customers
```

## Defining Methods with Attributes

As you've seen, you can define both methods (functions) and attributes of class objects. Here's a method that lets you update an attribute.


```python
class Business():
    def __init__(self, name=None, biz_type=None, city=None, customers = []):
        self.name = name
        self.biz_type = biz_type
        self.city = city
        self.customers = customers
    def add_customer(self, customer):
        self.customers.append(customer)
```

## Thinking about appropriate structures
At this point in creating our data structures, you can think about what you want a customer to be. It could be a dictionary storing various attributes about that customer such as name, orders, etc. It could also be a class of it's own. Thinking through the use case and allowing flexability is a key design decision.  

For maximum future flexability, you might define an additional class for customers like this:


```python
class Customer():
    def __init__(self, name=None, orders=[], location=None):
        self.name=name
        self.orders = orders
        self.location = location
    def add_order(item_name, item_cost, quantity):
        self.orders.append({'item_name': item_name, 'item_cost':item_cost, 'quantity':quantity})
```

## Writing more complicated methods using attriubtes

Imagine a reporting method for the business that will return the top 5 customers to date based on their purchase history. To do this, you'd have to determine the total purchases made by customers and then sort our customers by this. Currently the data needed for that is stored within a customer object within the orders attribute which is a list of dictionaries. Quite the mouthful there; an object with an attribute that's a list of dictionaries. Breaking down the problem into constituent parts can help reduce solving the same problems over and over again. As such, before writing a larger business function to retrieve the top 5 customers, a constituent piece is to update the customer object to also keep track of total spent.


```python
class Customer():
    def __init__(self, name=None, orders=[], location=None):
        self.name=name
        self.orders = orders
        self.location = location
        self.total_spent = sum([i['item_cost']*i['quantity'] for i in orders])
    def add_order(self, item_name, item_cost, quantity):
        self.orders.append({'item_name': item_name, 'item_cost':item_cost, 'quantity':quantity})
        self.total_spent += item_cost * quantity
```

Now the previous problem is greatly simplified; the customer objects directly have an attribute for the total spent. You can write a method for top customers with much greater ease:


```python
class Business():
    def __init__(self, name=None, biz_type=None, city=None, customers = []):
        self.name = name
        self.biz_type = biz_type
        self.city = city
        self.customers = customers
    def add_customer(self, customer):
        self.customers.append(customer)
    def top_n_customers(self, n):
        top_n = sorted(self.customers, key = lambda x: x.total_spent, reverse=True)[:n]
        for c in top_n:
            print(c.name, c.total_spent)
```

## Trying it out: Creating an Instance

Finally you can try it all out:


```python
startup = Business('etsy_store2076', 'crafts')
```


```python
customer1 = Customer(name='Bob', orders=[])
customer1.add_order('sweater', 24.99, 1)
```


```python
customer1.orders
```




    [{'item_cost': 24.99, 'item_name': 'sweater', 'quantity': 1}]




```python
customer1.total_spent
```




    24.99



## Generating Customers and orders at scale

Now you can systematically add some fake data to test the fancier method on. You can use some NumPy's built in random methods to randomly select quantities of orders and items.


```python
import numpy as np
```


```python
names = ['Liam',  'Emma', 'Noah','Olivia','William','Ava',
         'James','Isabella','Logan','Sophia','Benjamin','Mia','Mason',
         'Charlotte','Elijah','Amelia','Oliver','Evelyn','Jacob','Abigail]']
items = [('sweater',50), ('scarf', 35), ('gloves', 20), ('hat', 20)]

for i in range(10):
    customer = Customer(name=np.random.choice(names)) #Create a customer
    n_orders = np.random.randint(1,5) #Create an order or two, or three, or four, or five!
    for order_n in range(n_orders):
        idx = np.random.choice(len(items)) #np.random.choice doesn't work with nested lists; workaround
        item = items[idx]
        item_name = item[0]
        item_price = item[1]
        quantity = np.random.randint(1,4)
        customer.add_order(item_name, item_price, quantity)
    #Add the customer to our business
    startup.add_customer(customer)
```

## Trying out our complex method


```python
startup.top_n_customers(5)
```

    Isabella 1650
    Ava 1510
    Mia 1390
    Ava 1220
    Logan 1115



```python
startup.top_n_customers(50)
```

    Isabella 1650
    Ava 1510
    Mia 1390
    Ava 1220
    Logan 1115
    Ava 940
    James 780
    Olivia 630
    Benjamin 425
    Ava 185


## Summary
In this lesson, you were able to mimic a complex domain model using a Business and customer class with a few instance methods and variables.
