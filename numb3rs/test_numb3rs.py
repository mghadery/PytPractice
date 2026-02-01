import pytest
from numb3rs import validate

def test_validate():
    assert not validate("")
    assert not validate("1")
    assert not validate("1.1")
    assert not validate("1.1.1")
    assert not validate("1.1.1.1.")
    assert not validate("1.1.1.1.1")
    assert not validate("cat")
    assert not validate("1 1 1 1")
    assert not validate("1-1-1-1")
    assert not validate("1000.1.1.1")
    assert not validate("256.1.1.1")
    assert not validate("1.256.1.1")
    assert not validate("1.1.256.1")
    assert not validate("1.1.1.256")
    assert not validate("256.1.1.1")
    assert not validate("-1.1.1.1")
    assert validate("1.1.1.1")
    assert validate("0.0.0.0")
    assert validate("255.255.255.255")

