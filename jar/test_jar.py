from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert str(jar) == ""
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(1)
    assert jar.capacity == 1

    with pytest.raises(ValueError):
        Jar(-1)



def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"

    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit(-1)

    with pytest.raises(ValueError):
        jar = Jar(2)
        jar.deposit(3)


def test_withdraw():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(2)
    jar.withdraw(1)
    assert str(jar) == "🍪"

    with pytest.raises(ValueError):
        jar = Jar()
        jar.withdraw(1)

    with pytest.raises(ValueError):
        jar = Jar()
        jar.deposit(2)
        jar.withdraw(-1)
