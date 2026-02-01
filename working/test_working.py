import pytest
from working import convert

def test_convert():
    # assert convert("0:00 AM to 00:00 AM") == "00:00 to 00:00"
    assert convert("12:00 AM to 12:00 AM") == "00:00 to 00:00"
    # assert convert("0:00 PM to 00:00 PM") == "12:00 to 12:00"
    assert convert("12:00 PM to 12:00 PM") == "12:00 to 12:00"
    assert convert("11:59 AM to 11:59 AM") == "11:59 to 11:59"
    assert convert("11:59 PM to 11:59 PM") == "23:59 to 23:59"
    assert convert("1 AM to 2 PM") == "01:00 to 14:00"

    with pytest.raises(ValueError):
        assert convert("0:00AM to 00:00AM")

    with pytest.raises(ValueError):
        assert convert("0:00 AM  00:00 AM")

    with pytest.raises(ValueError):
        assert convert("0:00 AM - 00:00 AM")

    with pytest.raises(ValueError):
        assert convert("13:00 AM to 13:00 AM")

    with pytest.raises(ValueError):
        assert convert("0:60 AM to 00:60 AM")

    with pytest.raises(ValueError):
        assert convert(":00 AM to :00 AM")
