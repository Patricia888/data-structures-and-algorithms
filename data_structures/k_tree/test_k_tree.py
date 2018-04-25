from .k_tree import KTree as KT
from .k_tree import Node
import pytest


def test_node():
    """test K-tree node"""
    n = Node(1)
    assert n.val == 1
    assert n.children == []
    assert repr(n) == 'Node Val: 1'
    assert str(n) == 'Node value is 1'


def test_k_tree_repr_str(single_tree):
    """test KTree repr and str"""
    assert repr(single_tree) == '<Tree Root 1>'
    assert str(single_tree) == 'Tree root value is 1'


def test_insert_root_K_tree():
    """test insert"""
    tree = KT()
    tree.insert(1, None)
    assert tree.root.val == 1


def test_insert_children():
    """test insert"""
    tree = KT()
    tree.insert(1, None)
    tree.insert(2, 1)
    tree.insert(3, 1)
    child_vals = [node.val for node in tree.root.children]
    assert tree.root.val == 1
    assert tree.root.children[0].val == 2
    assert child_vals == [2, 3]


def test_insert_many_children():
    """test insert"""
    tree = KT()
    tree.insert(1, None)
    tree.insert(2, 1)
    tree.insert(3, 1)
    tree.insert(4, 3)
    tree.insert(5, 3)
    assert tree.root.val == 1
    assert tree.root.children[1].children[0].val == 4
    assert tree.root.children[1].children[1].val == 5


def test_insert_raise_error_parent_not_found():
    """test insert invalid"""
    tree = KT()
    tree.insert(1, None)
    with pytest.raises(ValueError) as err:
        tree.insert(2, 2)
        assert err == 'Parent value not found'


def test_insert_raise_error_none_parent():
    """test insert no parent value throws error"""
    tree = KT()
    tree.insert(1, None)
    with pytest.raises(ValueError) as err:
        tree.insert(2, None)
        assert err == 'Parent value not found'


def test_pre_order_small(small_tree):
    """test pre-order traversal of K-tree"""
    order = []
    small_tree.pre_order_traversal(lambda n: order.append(n.val))
    assert order == [1, 2, 3]


def test_pre_order_single(single_tree):
    """test pre-order traversal of K-tree"""
    order = []
    single_tree.pre_order_traversal(lambda n: order.append(n.val))
    assert order == [1]


def test_pre_order_tree(tree):
    """test pre-order traversal of K-tree"""
    order = []
    tree.pre_order_traversal(lambda n: order.append(n.val))
    assert order == [1, 2, 3, 4, 5]


def test_post_order_small(small_tree):
    """test post-order traversal of K-tree"""
    order = []
    small_tree.post_order_traversal(lambda n: order.append(n.val))
    assert order == [2, 3, 1]


def test_post_order_single(single_tree):
    """test post-order traversal of K-tree"""
    order = []
    single_tree.post_order_traversal(lambda n: order.append(n.val))
    assert order == [1]


def test_post_order_tree(tree):
    """test post-order traversal of K-tree"""
    order = []
    tree.post_order_traversal(lambda n: order.append(n.val))
    assert order == [2, 3, 4, 5, 1]


def test_breadth_first_traversal_small(small_tree):
    """test breadth-first traversal"""
    assert small_tree.breadth_first_traversal() == [1, 2, 3]


def test_breadth_first_traversal_single(single_tree):
    """test breadth-first traversal"""
    assert single_tree.breadth_first_traversal() == [1]


def test_breadth_first_traversal_tree(tree):
    """test breadth-first traversal"""
    assert tree.breadth_first_traversal() == [1, 2, 3, 4, 5]


def test_insert_all_root_K_tree():
    """test insert all method"""
    tree = KT()
    assert tree.insert_all(1, None) == '1 inserted at root'
    assert tree.root.val == 1


def test_insert_all_children_K_tree():
    """test insert all method"""
    tree = KT()
    tree.insert(1, None)
    tree.insert(2, 1)
    tree.insert(2, 1)

    child_vals = [node.val for node in tree.root.children]
    assert tree.root.val == 1
    assert tree.root.children[0].val == 2
    assert child_vals == [2, 2]
    assert tree.insert_all(5, 2) == '5 inserted 2 times'


def test_insert_all_many_children_K_tree():
    """test insert"""
    tree = KT()
    tree.insert(1, None)
    tree.insert(5, 1)
    tree.insert(3, 1)
    tree.insert(5, 3)
    tree.insert(5, 3)
    assert tree.root.val == 1
    assert tree.root.children[1].children[0].val == 5
    assert tree.root.children[1].children[1].val == 5
    assert tree.insert_all(10, 5) == '10 inserted 3 times'


def test_insert_all_raise_error_parent_not_found():
    """test insert all invalid parent throws error"""
    tree = KT()
    tree.insert(1, None)
    with pytest.raises(ValueError) as err:
        tree.insert_all(2, 2)
        assert err == 'Parent value not found'


def test_insert_all_raise_error_none_parent():
    """test insert all no parent value throws error"""
    tree = KT()
    tree.insert(1, None)
    with pytest.raises(ValueError) as err:
        tree.insert_all(2, None)
        assert err == 'Parent value not found'


def test_breadth_traversal_single(single_tree):
    """test breadth-first traversal"""
    order = []
    single_tree.breadth_first_traversal_op(lambda n: order.append(n.val))
    assert order == [1]


def test_breadth_traversal_small(small_tree):
    """test breadth-first traversal"""
    order = []
    small_tree.breadth_first_traversal_op(lambda n: order.append(n.val))
    assert order == [1, 2, 3]
