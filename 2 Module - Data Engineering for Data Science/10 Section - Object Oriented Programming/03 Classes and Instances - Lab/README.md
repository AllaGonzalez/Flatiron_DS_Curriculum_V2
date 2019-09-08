
# Classes and Instances - Lab

## Introduction
Okay, you'lve learned how to declare classes and create instances in the last lesson. Now it's time to put these new skills to the test!

## Objectives

You will be able to:

* Define classes
* Instantiate instances of classes

## Defining Classes


You're about to create your first packages with class definitions! You've already seen how to import packages such as NumPy and pandas, and you can organize your own code in a similar manner. For example, once you define the ride class in a file ride.py you can then import said code in another notebook or script with `import ride`. 

So without further ado, create three files in this folder: **ride.py**, **driver.py** and **passenger.py**. In each of these, define an accompanying class. By convention, you should capitalize the names of these classes within the .py file. For example, in the ride.py file, define a Ride class. For now, the classes need not do anything, just write the keyword `pass` on the first line under each of your class definitions.


```python
from ride import Ride
```


```python
# import Driver class here
```


```python
# import Passenger class here
```

## Creating Instances

Now practice using your classes to make instances of those classes. Make two instances of the Passenger class and assign them to the variables `meryl` and `daniel`, respectively.


```python
meryl = None
daniel = None
print(meryl, daniel)
```

Next, make one instance of the driver class and assign it to the variable, `flatiron_taxi`.


```python
flatiron_taxi = None
print(flatiron_taxi)
```

Finally, make two instances of the Ride class and assign them to `ride_to_school` and `ride_home`. 


```python
ride_to_school = None
ride_home = None
print(ride_to_school, ride_home)
```

## Summary
Great! In this lab, you were able to define multiple classes and create instances of those classes.
