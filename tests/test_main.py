from src.generated_code import hello

def test_hello_default():
    assert hello() == "Hello, World!"

def test_hello_name():
    assert hello("Sher") == "Hello, Sher!"

def test_hello_empty_string():
    assert hello("") == "Hello, !"

def test_hello_special_characters():
    assert hello("@User123") == "Hello, @User123!"
