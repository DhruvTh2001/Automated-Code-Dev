# tests/test_auto_output.py
from auto_output import greet

def test_greet():
    assert greet() == 'Hello, I am generated!'
