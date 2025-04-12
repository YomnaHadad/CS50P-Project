import pytest , builtins
from unittest import mock
from project import check_email , ordering , suggest

def test_check_email():
    assert check_email("name@domain.com") == True

def test_ordering():
    with mock.patch.object(builtins, "input", lambda _: "1"):
        assert ordering("1") == True

def test_suggest():
    with mock.patch.object(builtins, 'input', side_effect=['1']):
        result = suggest('2')
        assert result == True

