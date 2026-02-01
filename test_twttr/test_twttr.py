from twttr import shorten

def test_shorten_uppercase():
    assert shorten("FOOTBALL") == "FTBLL"
    assert shorten("QaoueiQ") == "QQ"

def test_shorten_lowercase():
    assert shorten("football") == "ftbll"
    assert shorten("qAOUEIq") == "qq"

def test_shorten_empty():
    assert shorten(" ") == " "
    assert shorten("") == ""

def test_shorten_numbers_spch():
    assert shorten("1234567890") == "1234567890"
    assert shorten('!@#$"_&*()') == '!@#$"_&*()'


if __name__ == "__main__":
    test_shorten()
