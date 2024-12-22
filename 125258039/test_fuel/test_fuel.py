from fuel import convert, gauge
import pytest


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_value():
    with pytest.raises(ValueError):
        convert("5/4")

def test_empty():
    assert gauge(convert("1/100")) == "E"

def test_full():
    assert gauge(convert("99/100")) == "F"

def test_half():
    assert convert("1/2") == 50
    assert gauge(50) == "50%"