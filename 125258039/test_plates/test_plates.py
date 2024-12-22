from plates import is_valid

def test_length():
    assert is_valid("HELLOWORLDYAYNOOKWHYNOT") == False

def test_lenght2():
    assert is_valid("A") == False

def test_ok():
    assert is_valid("HELLO") == True

def test_space():
    assert is_valid("WHY NOT") == False

def test_punct():
    assert is_valid("ADD,TOIT") == False

def test_nonalphanum():
    assert is_valid("AD!23") == False

def test_firstnum():
    assert is_valid("2345") == False

def test_nofirstzero():
    assert is_valid("CS05") == False

def test_twoalpha():
    assert is_valid("A50") == False

def test_endwithnum():
    assert is_valid("AAA22A") == False

def test_okok():
    assert is_valid("CS50") == True