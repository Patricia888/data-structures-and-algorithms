import pytest
from .queue import Queue


def test_make_valid_empty_queue(empty_queue):
    """Test that a new Queue has a back value of None"""
    assert empty_queue.front is None
    assert empty_queue.back is None
    assert len(empty_queue) == 0


def test_make_queue():
    """Test that a new queue is made"""
    q = Queue([1, 2, 3])
    assert q.front.val == 1
    assert q.back.val == 3
