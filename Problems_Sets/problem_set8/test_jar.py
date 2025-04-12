import pytest
from jar import Jar

def test_init():
    with pytest.raises(ValueError):
        jar = Jar(-1)

def test_str():
    jar2 = Jar()
    assert str(jar2) == ""
    jar2.deposit(1)
    assert str(jar2) == "🍪"
    jar2.deposit(11)
    assert str(jar2) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar3 = Jar()
    jar3.deposit(5)
    assert str(jar3) == "🍪🍪🍪🍪🍪"

def test_withdraw():
    jar4 = Jar(5)
    jar4.deposit(4)
    jar4.withdraw(2)
    assert str(jar4) == "🍪🍪"
