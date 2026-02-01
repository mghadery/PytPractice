from seasons import to_date, get_life_minutes
from datetime import date
import pytest

def test_to_date_correct():
    assert to_date("2025-01-02") == date(day=2, month=1, year=2025)


def test_to_date_incorrect():
    with pytest.raises(ValueError):
        to_date("2025-04-31")

    with pytest.raises(ValueError):
        to_date("2025-13-01")

    with pytest.raises(ValueError):
        to_date("20250101")

    with pytest.raises(ValueError):
        to_date("January 1, 1999")

def test_get_life_minutes():
    #normal year
    assert get_life_minutes(date(day=1, month=1, year=2023), date(day=1, month=1, year=2024)) == "Five hundred twenty-five thousand, six hundred"

    #leap year
    assert get_life_minutes(date(day=1, month=1, year=2024), date(day=1, month=1, year=2025)) == "Five hundred twenty-seven thousand forty"
