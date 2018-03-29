import pytest
from .linked_list import LinkedList as LL


def test_insert_first_node(empty_ll):
    assert empty_ll.head is None
    empty_ll.insert(2)
    assert empty_ll.head.val == 2


def test_insert_two_nodes(empty_ll):
    empty_ll.insert(2)
    empty_ll.insert(1)
    assert empty_ll.head.val == 1


def test_insert_iterable():
    assert LL([1, 2, 3, 4])._size == 4


def test_find_none(empty_ll):
    assert empty_ll.find(1) is False


def test_find(small_ll):
    assert small_ll.find(2) is True


def test_not_found(small_ll):
    assert small_ll.find(5) is False


def test_empty_list(empty_ll):
    assert len(empty_ll) == 0


def test_length(small_ll):
    assert len(small_ll) == 4


def test_check_valid_iterable():
    with pytest.raises(TypeError) as err:
        LL(2)

    assert str(err.value) == 'Invalid iterable'
