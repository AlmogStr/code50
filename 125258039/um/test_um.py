from um import count as f

def test_1():
    assert f("um") == 1

def test_2():
    assert f("um?") == 1

def test_3():
    assert f("Um. hi ,um") == 2

def test_4():
    assert f("yummy") == 0
