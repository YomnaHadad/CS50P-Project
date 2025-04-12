import pytest
from plates import is_valid

def test_length():
    assert is_valid("HELLO, WORLD") == False
    assert is_valid("HELLOWORLD") == False
    assert is_valid("HELLO") == True

def test_invalid_char():
    assert is_valid("Hi!!") == False
    assert is_valid("Hey ") == False

def test_all_number():
    assert is_valid("50") == False

def test_with_numbers():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True
    assert is_valid("33gg") == False
    assert is_valid("CS50P") == False

