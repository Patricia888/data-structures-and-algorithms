from .find_maximum_value_binary_tree import find_maximum_value, BST


def test_find_maximum_value_tree_with_one_value():
    one_value = BST([5])
    assert find_maximum_value(one_value) == 5


def test_find_maximum_value_tree_with_two_values():
    one_value = BST([10, 2])
    assert find_maximum_value(one_value) == 10


def test_find_maximum_value_balanced():
    balanced = BST([10, 7, 3, 16, 12, 8, 20])
    assert find_maximum_value(balanced) == 20


def test_find_maximum_value_left():
    left = BST([10, 8, 6, 4])
    assert find_maximum_value(left) == 10


def test_find_maximum_value_right():
    right = BST([1, 3, 5, 7, 9])
    assert find_maximum_value(right) == 9
