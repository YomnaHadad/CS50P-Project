import pytest
from fuel import convert, gauge

def test_Frac():
    assert convert("1/4") == 25
    assert gauge(25) == "25%"

def test_full_or_empty():
    assert gauge(99) == "F"
    assert gauge(1) == "E"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("c/s")
