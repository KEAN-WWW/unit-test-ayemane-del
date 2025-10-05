from app.calculator import Calculator

calc = Calculator()

def test_subtraction():
    assert calc.subtract(10, 4) == 6
    assert calc.subtract(0, 5) == -5
    assert calc.subtract(-3, -2) == -1
