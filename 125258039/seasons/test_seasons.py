from seasons import howmanydaysdoilive as f
import pytest

def test_mybirthday():
    assert f("1994-04-25") == "fifteen million, six hundred seventy-five thousand, eight hundred forty"

def test_oneday():
    assert f("2024-02-12") == "one thousand, four hundred forty"

def test_oops():
    try:
        assert f("January 1, 1990")
    except ValueError:
        pass

def test_oops2():
    with pytest.raises(ValueError):
        f("January 1, 1990")
