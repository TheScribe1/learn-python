    # this test_hello.py is inside tests folder , creating file name __init__.py makes this folder a package
from hello import hello

def test_argument():
        assert hello("David") == "Hello, David"

def test_default():
    assert hello() == "Hello, world"