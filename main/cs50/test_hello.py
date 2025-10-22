from hello import hello

def test_hello():
    assert hello("blaa") == "hello, blaa"

def test_blabla():
    assert hello() == "hello, world"

def test_bla():
    for name in ['Harry', 'Hermion', 'Ron']:
        assert hello(name) == f'hello, {name}'