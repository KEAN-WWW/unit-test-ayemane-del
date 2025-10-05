# app/calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


class Calculator:
    """Simple calculator using arithmetic functions."""

    def add(self, a, b):
        return add(a, b)

    def subtract(self, a, b):
        return subtract(a, b)

    def multiply(self, a, b):
        return multiply(a, b)

    def divide(self, a, b):
        return divide(a, b)
