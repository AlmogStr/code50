from twttr import shorten

def test_one():
    assert shorten("Hello World") == "Hll Wrld"

def test_two():
    assert shorten("hello world") == "hll wrld"

def test_three():
    assert shorten("WHAT?") == "WHT?"

def test_four():
    assert shorten("I Love CS50") == " Lv CS50"
