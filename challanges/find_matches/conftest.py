import pytest
from .k_tree import Node, KTree
from .queue import Queue

@pytest.fixture
def ktree_four_nodes():
    """ returns a ktree with a list of known values """
    ktree = KTree()
    ktree.insert(None, 1)
    ktree.insert(1, 2)
    ktree.insert(1, 3)
    ktree.insert(1, 4)
    return ktree

@pytest.fixture
def ktree_six_nodes():
    """ returns a ktree with a list of known values """
    ktree = KTree()
    ktree.insert(None, 1)
    ktree.insert(1, 2)
    ktree.insert(1, 2)
    ktree.insert(1, 4)
    ktree.insert(4, 2)
    ktree.insert(4, 6)
    return ktree

@pytest.fixture
def ktree_empty():
    """ returns empty ktree """
    return KTree()
