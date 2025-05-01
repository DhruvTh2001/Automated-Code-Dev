import os
import pytest

# Path to the generated code
generated_code_path = 'src/generated_code.py'

def test_generated_code_exists():
    """Test if the generated code file exists"""
    assert os.path.exists(generated_code_path), f"{generated_code_path} does not exist"

def test_generated_code_function():
    """Test if the generated function exists and is correct"""
    with open(generated_code_path, 'r') as file:
        code = file.read()
    
    # Check that the function is in the generated code
    assert "def auto_generated_function" in code, "Function auto_generated_function not found"
    
def test_generated_code_message():
    """Test if the generated message is correct"""
    with open(generated_code_path, 'r') as file:
        code = file.read()
    
    # Check that the message is correctly replaced
    assert "This function was generated automatically!" in code, "Message not found in generated code"

def test_function_execution():
    """Test if the function in generated code runs correctly"""
    # Execute the generated code and check output
    from src.generated_code import auto_generated_function
    from io import StringIO
    import sys

    # Capture the print output
    captured_output = StringIO()
    sys.stdout = captured_output
    auto_generated_function()  # Call the function

    # Check if the function prints the expected message
    assert captured_output.getvalue().strip() == "This function was generated automatically!", \
        "Function output does not match expected message"
