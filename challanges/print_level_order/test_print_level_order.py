from k_tree import KTree as KT
from print_level_order import print_level_order
import pytest


@pytest.fixture
def single_tree():
    tree = KT()
    tree.insert(1, None)
    return tree


@pytest.fixture
def small_tree():
    tree = KT()
    tree.insert(1, None)
    tree.insert(2, 1)
    tree.insert(3, 1)
    return tree


@pytest.fixture
def tree():
    tree = KT()
    tree.insert(1, None)
    tree.insert(2, 1)
    tree.insert(3, 1)
    tree.insert(4, 1)
    tree.insert(5, 1)
    return tree

