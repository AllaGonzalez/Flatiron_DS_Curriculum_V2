# importing testing framwork
import pytests
# library used to check working virtual environment
import importlib

# importing objects from the jupyter notebook here
from ipynb.fs.full.index import ceo, art_vandelay, ends_with_com, web_address, phone_num_one, phone_num_two

# tests to ensure correct environment is loaded
def test_conda_environment_activated():
    assert importlib.util.find_spec("obscure"), "It looks like you didn't 'conda activate learn-env' - try that then run the test again!"

def test_ceo():
    assert type(ceo) == type(""), "the variable, ceo, must be assigned to a string"
    assert ceo == "CEO", "the string assigned to ceo must be in all capital letters, CEO"

def test_art_vandelay():
    assert type(art_vandelay) == type(""), "the variable, art_vandelay, must be assigned to a string"
    assert art_vandelay == "Art Vandelay", "the string assigned to art_vandelay must be in title case"

def test_ends_with_com():
    assert type(ends_with_com) == type(True), "the variable, ends_with_com, must be assigned to a Boolean value"
    assert ends_with_com == False, "You must use a string method to test whether the string *ends with* `.com`, and return a boolean value of True or False"

def test_web_address():
    assert type(web_address) == type(""), "the variable, web_address, must be assigned to a string"
    assert web_address == "www.vandelay.com", "the string assigned to web_address must be prepended with www. -- think about how to add www. to the beginning of a string"

def test_phone_num_one():
    assert type(phone_num_one) == type(100), "the variable, phone_num_one, must be assigned to a integer"
    assert phone_num_one == 7285553335, "the integer assigned to phone_num_one must be one number more than the string 7285553334"

def test_phone_num_two():
    assert type(phone_num_two) == type(100), "the variable, phone_num_two, must be assigned to a integer"
    assert phone_num_two == 7285553336, "the integer assigned to phone_num_two must be two numbers more than the string 7285553334"
