from working import convert as f
import pytest

def test_norm():
    assert f("9 AM to 5 PM") == "09:00 to 17:00"

def test_outh():
    try:
        assert f("13 AM to 5 PM")
    except ValueError:
        pass
    
def test_outmin2():
    with pytest.raises(ValueError):
        f("9:60 AM to 5:61 PM")

def test_outmin():
    try:
        assert f("9:60 AM to 5:61 PM")
    except ValueError:
        pass

def test_syntax():
    try:
        assert f("9 AM - 5 PM")
    except ValueError:
        pass

def test_norm2():
    assert f("10:30 PM to 8:50 AM") == "22:30 to 08:50"
