import importlib
from ipynb.fs.full.index import x

def test_conda_environment_activated():
    assert importlib.util.find_spec("obscure"), "It looks like you didn't 'conda activate learn-env' - try that then run the test again!"

def test_access_to_notebook():
    assert x == 4, "The importing of values from the notebook does not appear to be working correctly"

def test_designed_to_fail():
    assert x == 3, "This test *should* fail - if it doesn't, something is wrong!"