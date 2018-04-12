from .bst import BST
from .bst import Node
import pytest


def test_create_node():
    node = Node(5)
    assert node.left is None
    assert node.right is None


def test_bst_created_with_iterable():
    binarytree = BST([1, 2, 3])
    assert binarytree.root.val == 1
    assert binarytree.root.right.val == 2
    assert binarytree.root.right.right.val == 3


