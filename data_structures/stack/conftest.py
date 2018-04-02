import pytest
from .stack import Stack


@pytest.fixture
def empty_stack():
    """empty stack"""
    return Stack()
