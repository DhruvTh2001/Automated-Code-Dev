# tests/test_main.py
import sys
import os

# Add src to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from generated_code import auto_generated_function

def test_auto_generated_function(capsys):
    auto_generated_function()
    captured = capsys.readouterr()
    assert "generated automatically" in captured.out
