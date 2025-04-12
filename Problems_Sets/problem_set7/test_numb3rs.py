import pytest
from numb3rs import validate

def test_True_validate():
    assert validate("1.2.3.4") == True
    assert validate("4.128.255.88") == True

def test_False_validate():
    assert validate("275.2.3.4") == False
    assert validate("7.250.333.40") == False
    assert validate("cat") == False
