from .binary_search import BinarySearch
import pytest


def test_BinarySearch_example_one():
    assert BinarySearch([4, 8, 15, 16, 23, 42], 15) == 2


def test_BinarySearch_example_two():
    assert BinarySearch([11, 22, 33, 44, 55, 66, 77], 90) == -1
