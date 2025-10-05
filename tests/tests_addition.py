from app.calculator import Calculator

calc = Calculator()

def test_addition():
    assert calc.add(5, 3) == 8
    assert calc.add(-2, 2) == 0
    assert calc.add(-4, -6) == -10
