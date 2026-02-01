from plates import is_valid

def main():
    test_is_valid_length()

def test_is_valid_length():
    assert not is_valid("C")
    assert is_valid("CS")
    assert is_valid("CS1501")
    assert not is_valid("CS15012")

def test_is_valid_start_2char():
    assert not is_valid("12")
    assert not is_valid("C1")
    assert is_valid("CS")
    assert is_valid("CSS")

def test_is_valid_alpha():
    assert not is_valid("CS!")
    assert not is_valid("CS@")
    assert not is_valid("CS#")
    assert not is_valid("CS$")
    assert not is_valid("CS%")
    assert not is_valid("CS^")

def test_is_valid_numbers_only_end():
    assert not is_valid("CS50C")

def test_is_valid_first_non_zero():
    assert not is_valid("CS050")
