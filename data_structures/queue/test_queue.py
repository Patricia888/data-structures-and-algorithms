import pytest
from .queue import Queue


def test_make_valid_empty_queue(empty_queue):
    assert empty_queue.front is None
    assert empty_queue.back is None
    assert len(empty_queue) == 0


def test_make_queue():
    q = Queue([1, 2, 3])
    assert q.front.val == 1
    assert q.back.val == 3


def test_make_invalid_queue():
    with pytest.raises(TypeError) as err:
        Queue(1)
    assert str(err.value) == 'Invalid iterable'


def test_enqueue_single(empty_queue):
    empty_queue.enqueue(20)
    assert empty_queue.front.val == 20
    assert empty_queue.back.val == 20
    assert len(empty_queue) == 1


def test_enqueue(short_queue):
    short_queue.enqueue(6)
    assert short_queue.front.val == 1
    assert short_queue.back.val == 6
    assert len(short_queue) == 6


def test_enqueue_long(long_queue):
    long_queue.enqueue(11)
    assert long_queue.front.val == 1
    assert long_queue.back.val == 11
    assert len(long_queue) == 11


def test_dequeue(short_queue):
    assert short_queue.dequeue() == 1
    assert len(short_queue) == 4


def test_dequeue_values(short_queue):
    short_queue.dequeue()
    assert short_queue.front.val == 2
    assert short_queue.back.val == 5


def test_dequeue_long(long_queue):
    assert long_queue.dequeue() == 1
    assert len(long_queue) == 9


def test_dequeue_long_values(long_queue):
    long_queue.dequeue()
    assert long_queue.front.val == 2
    assert long_queue.back.val == 10


def test_dequeue_raise_error(empty_queue):
    with pytest.raises(IndexError) as err:
        empty_queue.dequeue()
    assert str(err.value) == 'List is empty'
