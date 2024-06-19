"""
Unit tests for arithmetic module functions.
"""

import pytest
from arithmetic import add, subtract, multiply, divide

def test_add():
    """Test addition of two numbers."""
    assert add(1, 2) == 3

def test_subtract():
    """Test subtraction of two numbers."""
    assert subtract(2, 1) == 1

def test_multiply():
    """Test multiplication of two numbers."""
    assert multiply(2, 3) == 6

def test_divide():
    """Test division of two numbers."""
    assert divide(6, 2) == 3

def test_divide_by_zero():
    """Test division by zero raises ValueError."""
    with pytest.raises(ValueError):
        divide(1, 0)

# Ensure there's a newline at the end of the file.
