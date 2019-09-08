import pytest
from ipynb.fs.full.index import Passenger, Driver, driver, passenger, find_driver_by_name, alex_driver, michelle_driver, jake_driver, ashleigh_driver, list_of_drivers, name_starts_with, highest_rated_driver

def create_example_class():
    class Example:
        pass
    return Example

def test_classes():
    assert Passenger
    assert Driver
    assert type(Passenger) == type(create_example_class())
    assert type(Driver) == type(create_example_class())

def test_instances():
    assert driver is not None
    assert passenger is not None
    assert type(driver) == type(Driver())
    assert type(passenger) == type(Passenger())

def test_find_driver_by_name_func():
    assert type(list_of_drivers) == type([])
    assert find_driver_by_name(list_of_drivers, 'ashleigh') == ashleigh_driver
    assert find_driver_by_name(list_of_drivers, 'Aziz') == "Sorry we couldn't find a driver with the name, Aziz! :("

def sort_lists_by_name(list):
    return sorted(name_starts_with(list_of_drivers, 'a'), key=lambda driver: driver.name)

def test_name_starts_with():
    assert sort_lists_by_name(name_starts_with(list_of_drivers, 'a')) == [alex_driver, ashleigh_driver]
    assert name_starts_with(list_of_drivers, 'al') == [alex_driver]
    assert name_starts_with(list_of_drivers, 'az') == []

def create_jack_driver_instance():
    jack_driver = Driver()
    jack_driver.name = "jack"
    jack_driver.rating = 10.0
    return jack_driver

def test_highest_rated_driver():
    jack = create_jack_driver_instance()
    list_of_drivers.append(jack)
    assert highest_rated_driver(list_of_drivers) is jack
