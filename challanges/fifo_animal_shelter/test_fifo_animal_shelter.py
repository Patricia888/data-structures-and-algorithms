from fifo_animal_shelter import AnimalShelter
import pytest


def test_empty_shelter(empty_queue):
    assert empty_queue.front is None
    assert empty_queue.back is None
    assert empty_queue._size == 0
