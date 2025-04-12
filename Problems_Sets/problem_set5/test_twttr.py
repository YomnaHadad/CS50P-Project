import pytest
from twttr import shorten

def test_word():
    assert shorten("Twitter") == "Twttr"
    assert shorten("TwittEr!") == "Twttr!"

def test_with_nums():
    assert shorten("UserS21") == "srS21"


