import Calculator

import pytest

@pytest.mark.xfail
@pytest.mark.parametrize("a, b, c", [(7, 3, 6,), (4, 3, 7), (5, 8, 14), (7, 14, 21)])
def test_add_two_num(a, b, c):

    Res = Calculator.add_two_num(a, b)
    assert Res == c
# @pytest.mark.addsub      # Grouping method using mark and marker name !!!
# def test_add_two_num():
#     x = 10
#     y = 20
#     Res = Calculator.add_two_num(x, y)
#     assert Res == x + y




@pytest.mark.parametrize("a, b, c", [(8, 13, -9), (3, 9, -2), (5, 10, -14)])
def test_sub_two_num(a, b, c):

    Res = Calculator.sub_two_num(a, b)
    assert Res == c
# @pytest.mark.addsub
# def test_sub_two_num():     # we must have to determine the same word in the test case function !!!
#     x = 10
#     y = 20
#     Res = Calculator.sub_two_num(x, y)
#     assert Res == x - y                 # Assert is for checking the operation and the values are equal or not !!!




@pytest.mark.parametrize("a, b, c", [(3, 14, -9), (8, 1, -3), (5, 12, 4)])
def test_mul_two_num(a, b, c):

    Res = Calculator.mul_two_num(a, b)
    assert Res == c
# @pytest.mark.muldiv
# def test_mul_two_num():
#     x = 10
#     y = 20
#     Res = Calculator.mul_two_num(x, y)
#     assert Res == x * y




@pytest.mark.parametrize("a, b, c", [(1, -16, 9), (2, 15, -12),(2, 8, 4)])
@pytest.mark.muldiv
@pytest.mark.skip(reason="No Need")
def test_div_two_num(a, b, c):

    Res = Calculator.div_two_num(a, b)
    assert Res == c
# @pytest.mark.muldiv
# def test_div_two_num():
#     x = 10
#     y = 20
#     Res = Calculator.div_two_num(x, y)
#     assert Res == x / y
