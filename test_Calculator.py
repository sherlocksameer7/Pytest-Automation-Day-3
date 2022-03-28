import Calculator


def test_add():
    x = 10
    y = 20
    Res = Calculator.add_two_num(x,y)
    assert Res == x+y

def test_sub():
    x = 10
    y = 20
    Res = Calculator.sub_two_num(x, y)
    assert Res == x - y                 # Assert is for checking the operation and the values are equal or not !!!

def test_mul():
    x = 10
    y = 20
    Res = Calculator.mul_two_num(x, y)
    assert Res == x * y

def test_div():
    x = 10
    y = 20
    Res = Calculator.div_two_num(x, y)
    assert Res == x / y
