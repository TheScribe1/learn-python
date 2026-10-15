                #   Unit Test - A unit test checks that a small unit(function, method, small class) of code behaves correctly.




# from calculator import square


# def main():
#     test_square()   # Testing frameworks discover tests automatically if test_ used as Prefix

# def test_square():
#     # if square(2) != 4 :
#     #     print("2 square was not 4")
#     # if square(3) != 9 :
#     #     print("3 square was not 9")
#     try:
#         assert square(2) == 4   # assert is a debugging statement used to test whether a condition is true. If the condition is false, Python raises an AssertionError.
#     except:
#         print("2 squared was not 4")
#     try:
#         assert square(3) == 9
#     except:
#         print("3 squared was not 9")
#     try:
#         assert square(0) == 0
#     except:
#         print("0 squared was not 0")
#     try:
#         assert square(-3) == 9
#     except:
#         print("-3 squared was not 9")
    
    

# if __name__ == "__main__":
#     main()







                #   pytest is a popular Python testing framework that makes writing and running tests easier.



import pytest
from calculator import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):  #   I expect the code inside this block to raise a TypeError
        square("cat")

# to run pytest, write in terminal : pytest file_name or pytest