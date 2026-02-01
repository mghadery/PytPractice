from bank import value

def main():
    test_value_hello()
    test_value_hi()
    test_value_others()

def test_value_hello():
    assert 0 == value("HELLO")
    assert 0 == value("HELLO123")
    assert 100 == value("123HELLO")
    assert 0 == value("hello")
    assert 0 == value("hello123")
    assert 100 == value("123hello")

def test_value_hi():
    assert 20 == value("HI")
    assert 20 == value("HI123")
    assert 100 == value("123HI")
    assert 20 == value("hi")
    assert 20 == value("hi123")
    assert 100 == value("123hi")

def test_value_others():
    assert 100 == value(" ")
    assert 100 == value("Ciao")
    assert 100 == value("123")
    assert 100 == value('!@#$%^&*()')

if __name__ == "__main__":
    main()
