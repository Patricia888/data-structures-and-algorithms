import pytest
from .stack import Stack


@pytest.fixture
def empty_stack():
    """empty stack"""
    return Stack()


@pytest.fixture
def short_stack():
    """push values in for a short stack for testing"""
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    return s


@pytest.fixture
def tall_stack():
    """Create a tall stack"""
    s = Stack()
    for num in range(1, 11):
        s.push(num)
    return s
