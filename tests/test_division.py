"""Unit tests for the division functionality of the Calculator class."""

import pytest
from app.calculator import Calculator

def test_division():
    """Test division with positive, negative, and fractional results."""
    calc = Calculator()
    assert calc.divide(10, 2) == 5
    assert calc.divide(-15, 3) == -5
    assert calc.divide(9, 2) == 4.5

def test_divide_by_zero():
    """Test division by zero raises ValueError."""
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(10, 0)
