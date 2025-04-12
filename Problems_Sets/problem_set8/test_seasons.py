import pytest
from seasons import calculate

def test_main():
    assert calculate("1999-01-01") == "Thirteen million, five hundred twenty-four thousand, four hundred eighty"
