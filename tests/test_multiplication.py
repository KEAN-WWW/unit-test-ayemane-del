from app.calculator import Calculator

calc = Calculator()

def test_multiplication():
    assert calc.multiply(6, 7) == 42
    assert calc.multiply(-3, 3) == -9
    assert calc.multiply(0, 100) == 0
