import pytest
from bank import value

def test_for_0():
    assert value("HELLO") == 0

def test_for_25():
    assert value("Hey") == 20
    assert value("hey") == 20

def test_for_100():
    assert value("What's up?") == 100
