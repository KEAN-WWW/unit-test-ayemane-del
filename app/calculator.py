"""Simple calculator module with basic arithmetic operations."""

def add(a, b):
    """Return the sum of two numbers a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b (a - b)."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers a and b."""
    return a * b

def divide(a, b):
    """
    Return the division of a by b (a / b).

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


class Calculator:
    """Simple calculator class using arithmetic functions."""

    def add(self, a, b):
        """Return the sum of a and b using the add function."""
        return add(a, b)

    def subtract(self, a, b):
        """Return the difference of a and b using the subtract function."""
        return subtract(a, b)

    def multiply(self, a, b):
        """Return the product of a and b using the multiply function."""
        return multiply(a, b)

    def divide(self, a, b):
        """Return the division of a by b using the divide function."""
        return divide(a, b)
