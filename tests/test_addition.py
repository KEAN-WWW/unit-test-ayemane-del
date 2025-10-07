"""Unit tests for the addition functionality of the Calculator class."""

from app.calculator import Calculator

def test_addition():
    """Test addition with positive and negative integers."""
    calc = Calculator()
    assert calc.add(5, 3) == 8
    assert calc.add(-2, 2) == 0
    assert calc.add(-4, -6) == -10
