import pytest
from .queue import Queue


@pytest.fixture
def empty_queue():
    """empty queue"""
    return Queue()
