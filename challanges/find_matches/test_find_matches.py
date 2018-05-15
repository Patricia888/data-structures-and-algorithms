from .k_tree import Node, KTree
from .find_matches import find_matches
import pytest


def test_find_match(ktree_four_nodes):
    """Tests find_matches function with valid input and one match."""
    assert find_matches(
        ktree_four_nodes, 2) == [ktree_four_nodes.root.children[0]]


def test_find_matches(ktree_six_nodes):
    """Test find_matches function with valid input and 3 matches."""
    test_list = [
        ktree_six_nodes.root.children[0],
        ktree_six_nodes.root.children[1],
        ktree_six_nodes.root.children[2].children[0],
    ]
    assert find_matches(ktree_six_nodes, 2) == test_list


def test_invalid_input():
    """Test find_matches function with invalid input."""
    assert find_matches(1,2) == False


def test_find_no_matches(ktree_empty):
    """Tests find_matches function with valid input and no matches."""
    assert find_matches(
        ktree_empty, 10) == []


def test_ktree_root(ktree_four_nodes):
    """Tests self.root of the ktree."""
    assert ktree_four_nodes.root.val == 1


def test_ktree_empty_root(ktree_empty):
    """Tests for self.root on passed empty ktree."""
    assert ktree_empty.root is None


def test__repr__(ktree_four_nodes):
    """Tests repr for tree ."""
    assert ktree_four_nodes.root.val == 1


def test_ktree_insert(ktree_empty):
    """Tests instert method."""
    ktree_empty.insert(None, 1)
    assert ktree_empty.root.val == 1
    ktree_empty.insert(1, 3)
    assert ktree_empty.root.children[0].val == 3


def test_children_of_tree(ktree_four_nodes):
    """Checks different parts of nodes ."""
    assert ktree_four_nodes.root.val == 1
    assert ktree_four_nodes.root.children[0].val == 2
    assert ktree_four_nodes.root.children[1].val == 3
    assert ktree_four_nodes.root.children[2].val == 4
    assert ktree_four_nodes._size == 4


def test_ktree_breadth_first_traversal_normal(ktree_four_nodes):
    """Tests ktree comes out in correct order."""
    assert ktree_four_nodes.breadth_first_traversal(
        lambda x: print('x')) == [1, 2, 3, 4]


def test_ktree_pre_order_traversal_normal(ktree_four_nodes):
    """Tests ktree comes out in correct order."""
    check_list = []
    ktree_four_nodes.pre_order_traversal(lambda x: check_list.append(x.val))
    assert check_list == [1, 2, 3, 4]


def test_ktree_post_order_traversal_normal(ktree_four_nodes):
    """Tests ktree comes out in correct order."""
    check_list = []
    ktree_four_nodes.post_order_traversal(lambda x: check_list.append(x.val))
    assert check_list == [2, 3, 4, 1]
