# tests/test_main.py

from src.generated_code import auto_generated_function

def test_auto_generated_function_output(capfd):
    """Test if the auto-generated function prints the correct output"""
    output = auto_generated_function()
    assert output == "This function was generated automatically!"
