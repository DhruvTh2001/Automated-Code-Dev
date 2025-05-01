import sys
import os

# Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from generated_code import hello  # adjust this if your function is named differently

def test_hello():
    assert hello() == "Hello World"  # replace with actual expected output if different
