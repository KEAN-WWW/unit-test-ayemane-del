"""Unit tests for the subtraction functionality of the Calculator class."""

from app.calculator import Calculator

def test_subtraction():
    """Test subtraction with positive, zero, and negative numbers."""
    calc = Calculator()
    assert calc.subtract(10, 4) == 6
    assert calc.subtract(0, 5) == -5
    assert calc.subtract(-3, -2) == -1
