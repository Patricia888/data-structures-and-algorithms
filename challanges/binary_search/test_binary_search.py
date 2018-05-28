# from .binary_search import BinarySearch
from .binary_search import binary_search
import pytest


# def test_BinarySearch_example_one():
#     assert BinarySearch([4, 8, 15, 16, 23, 42], 15) == 2


# def test_BinarySearch_example_two():
#     assert BinarySearch([11, 22, 33, 44, 55, 66, 77], 90) == -1


def test_BinarySearch_example_one():
    assert binary_search([4, 8, 15, 16, 23, 42], 15) == 2


def test_BinarySearch_no_result():
    assert binary_search([1, 2, 3, 4], 6) == -1


def test_BinarySearch_empty_array():
    assert binary_search([], 5) == -1
