from assignment import *
import pytest
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-5, -3) == -8

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(-3, -7) == 4
    assert subtract(10, 10) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 100) == 0
    assert multiply(-4, -6) == 24

def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(-10, 2) == -5
    assert divide(-9, -3) == 3
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_perimeter():
    assert perimeter(5, 3) == 16
    assert perimeter(0, 0) == 0
    assert perimeter(7, 2) == 18
    assert perimeter(10, 10) == 40

def test_area():
    assert area(5, 3) == 15
    assert area(0, 10) == 0
    assert area(7, 2) == 14
    assert area(10, 10) == 100
