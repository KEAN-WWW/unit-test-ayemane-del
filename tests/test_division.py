# tests/test_division.py

import pytest
from app.calculator import Calculator

calc = Calculator()

def test_division():
    assert calc.divide(10, 2) == 5
    assert calc.divide(-15, 3) == -5
    assert calc.divide(9, 2) == 4.5  # Optional: test float result

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calc.divide(10, 0)
