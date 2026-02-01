from um import count

def test_count():
    assert count('') == 0
    assert count('umm') == 0
    assert count('um umm um') == 2
    assert count('um um umm') == 2
    assert count('sum um um') == 2
    assert count('um sum um') == 2
    assert count('um um sum') == 2
    assert count('Um') == 1
    assert count('uM1') == 0
    assert count('uM.') == 1
    assert count('.uM.') == 1
    assert count('.uM.um') == 2
