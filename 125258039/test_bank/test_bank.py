from bank import value


def test_hello():
    assert value("hello") == 0

def test_Hello():
    assert value("Hello there") == 0

def test_hey():
    assert value("Hey there!") == 20

def test_nothing():
    assert value("jesus good morning") == 100