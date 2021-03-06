from .breadth_first_traversal import BST
from .breadth_first_traversal import breadth_first_traversal


def test_breadth_first_traversal():
    tree = BST([2, 1, 3])
    assert breadth_first_traversal(tree) == [2, 1, 3]


def test_breadth_first_traversal_only_root():
    tree = BST([1])
    assert breadth_first_traversal(tree) == [1]


def test_breadth_first_traversal_not_a_number():
    tree = BST(['cat', 'dog'])
    assert breadth_first_traversal(tree) == ['cat', 'dog']


def test_breadth_first_traversal_empty_tree():
    tree = BST([])
    assert breadth_first_traversal(tree) == []


def test_breadth_first_traversal_balanced():
    tree = BST([10, 7, 3, 16, 12, 8, 20])
    assert breadth_first_traversal(tree) == [10, 7, 16, 3, 8, 12, 20]


def test_breadth_first_traversal_right():
    tree = BST([1, 3, 5, 7, 9])
    assert breadth_first_traversal(tree) == [1, 3, 5, 7, 9]
