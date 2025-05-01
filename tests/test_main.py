from generated_code import auto_generated_function

def test_auto_generated_function_output(capfd):
    output = auto_generated_function()
    assert output == "This function was generated automatically!"
