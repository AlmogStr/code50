from numb3rs import validate as f

def test_min():
    assert f("0.0.0.0") == True

def test_max():
    assert f("255.255.255.255") == True

def test_overmax():
    assert f("256.0.0.0") == False

def test_overmax2():
    assert f("0.256.256.256") == False

def test_letters():
    assert f("A.0.0.0") == False
