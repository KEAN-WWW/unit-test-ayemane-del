import pytest
from app.calculator import Calculator

calc = Calculator()

def test_division():
    assert calc.divide(10, 2) == 5
    assert calc.divide(-15, 3) == -5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calc.divide(10, 0)
