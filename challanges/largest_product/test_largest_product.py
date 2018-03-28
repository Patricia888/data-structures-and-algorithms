from .largest_product import largest_product
import pytest


def test_largest_product_example_one():
    assert largest_product([[1, 2], [3, 4], [5, 6], [7, 8]]) == 56


def test_largest_product_example_two():
    assert largest_product([[1, 2], [1, 1], [3, 10], [3, 3], [20, 2]]) == 40
