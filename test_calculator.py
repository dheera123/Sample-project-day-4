import pytest
from calculator import add, subtract, multiply, divide


def test_add():
    pass


def test_subtract():
    pass


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(5, 2) == 10
    assert multiply(-2, 3) == -6


def test_divide():
    assert divide(10, 2) == 5
    assert divide(15, 3) == 5
    assert divide(7, 2) == 3.5
    
    # Test division by zero raises ValueError
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
