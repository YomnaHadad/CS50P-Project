import pytest
from working import convert

def test_1():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"

def test_2():
    with pytest.raises(ValueError):
        convert("9 AM - 17 PM")
    with pytest.raises(ValueError):
        convert("9:20 AM 5:29 PM")
    with pytest.raises(ValueError):
        convert("9AM to 2PM")

def test_3():
    with pytest.raises(ValueError):
        convert("16:01 AM to 12:30 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 1:60 PM")

