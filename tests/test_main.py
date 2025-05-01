import sys
import os
from datetime import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from generated_code import auto_generated_function

def test_function_execution():
    """Test if the function in generated code runs correctly"""
    assert auto_generated_function() == "This function was generated automatically!"

def test_auto_generated_function_output(capfd):
    """Test if the auto-generated function prints the correct output"""
    auto_generated_function()
    captured = capfd.readouterr()
    assert captured.out.strip() == "This function was generated automatically!"
