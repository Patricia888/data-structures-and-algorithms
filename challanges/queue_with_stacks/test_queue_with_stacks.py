from .queue_with_stacks import Queue
import pytest


def test_make_queue():
    q = Queue([1, 2, 3, 4])
    assert q.stack_one.top.val == 4
    assert q.stack_one._size == 4
    assert q._size == 4

