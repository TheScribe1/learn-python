from hello import hello

def test_argument():    #   testing every function separately gives accurate clear testing output 
    for name in ["Hermione", "Henry", "Ron"]:
        assert hello(name) == f"Hello, {name}"

def test_default():
    assert hello() == "Hello, world"