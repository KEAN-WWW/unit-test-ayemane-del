"""Unit tests for the multiplication functionality of the Calculator class."""

from app.calculator import Calculator

def test_multiplication():
    """Test multiplication with positive, negative, and zero values."""
    calc = Calculator()
    assert calc.multiply(6, 7) == 42
    assert calc.multiply(-3, 3) == -9
    assert calc.multiply(0, 100) == 0
