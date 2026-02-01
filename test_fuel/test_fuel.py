import pytest
from fuel import convert, gauge

def test_convert_exceptions():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("1")

    with pytest.raises(ValueError):
        convert("1.1/1")

    with pytest.raises(ValueError):
        convert("1/1.1")

    with pytest.raises(ValueError):
        convert("a/1")

    with pytest.raises(ValueError):
        convert("1/a")

    with pytest.raises(ValueError):
        convert("5/4")

    #with pytest.raises(ValueError):
    #    convert("-1/1")

    #with pytest.raises(ValueError):
    #    convert("1/-1")

def test_convert():
    assert convert("0/2") == 0
    assert convert("1/2") == 50
    assert convert("4/4") == 100

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
