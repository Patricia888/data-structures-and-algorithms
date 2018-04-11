import pytest
from .ll_find_loop import LinkedList as LL
# from .ll_mergeLists import merge_lists as ml


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


def test_len_increases(empty_ll):
    assert len(empty_ll) == 0
    empty_ll.insert(1)
    assert len(empty_ll) == 1


def test_check_valid_iterable():
    with pytest.raises(TypeError) as err:
        LL(2)

    assert str(err.value) == 'Invalid iterable'


def test_append_to_end_empty(empty_ll):
    empty_ll.append(2)
    assert empty_ll.head.val == 2


def test_append_to_end(small_ll):
    small_ll.append(5)
    assert len(small_ll) == 5
    assert small_ll.head._next._next._next._next.val == 5


def test_insert_after(small_ll):
    small_ll.insert_after(2, 8)
    assert len(small_ll) == 5
    assert small_ll.head._next._next.val == 8


def test_insert_after_end(small_ll):
    small_ll.insert_after(4, 9)
    assert len(small_ll) == 5
    assert small_ll.head._next._next._next._next.val == 9


def test_insert_after_invalid(small_ll):
    small_ll.insert_after(6, 9)
    assert len(small_ll) == 4


def test_insert_before(small_ll):
    small_ll.insert_before(3, 6)
    assert len(small_ll) == 5
    assert small_ll.head._next._next.val == 6


def test_insert_before_head(small_ll):
    small_ll.insert_before(1, 7)
    assert len(small_ll) == 5
    assert small_ll.head.val == 7


def test_insert_before_invalid(small_ll):
    small_ll.insert_before(6, 7)
    assert len(small_ll) == 4


def test_kth_from_end_last(small_ll):
    small_ll.kth_from_end(0)
    assert small_ll.head._next._next._next.val == 4


def test_kth_from_end_second(small_ll):
    small_ll.kth_from_end(2)
    assert small_ll.head._next.val == 2


def test_kth_from_end_exception(small_ll):
    with pytest.raises(AttributeError):
        small_ll.kth_from_end(6)
        small_ll.kth_from_end(-1)


def test_kth_from_end_invalid(small_ll):
    with pytest.raises(TypeError):
        small_ll.kth_from_end('a')


# test list merging
# def test_merge_list(short_ll, long_ll):
#     assert ml(short_ll, long_ll) == 5
#     assert len(long_ll) == 10


# def test_merge_list_values(short_ll, long_ll):
#     ml(short_ll, long_ll)
#     assert long_ll.head.val == 5
#     assert long_ll.head._next.val == 11


# def test_merge_list_two(long_ll, short_ll):
#     assert ml(long_ll, short_ll) == 11
#     assert len(long_ll) == 10


# def test_merge_list_two_values(long_ll, short_ll):
#     ml(long_ll, short_ll)
#     assert long_ll.head.val == 11
#     assert long_ll.head._next.val == 5


# def test_merge_list_same(short_ll, small_ll):
#     assert ml(short_ll, small_ll) == 5
#     assert len(small_ll) == 8


# def test_merge_list_same_values(short_ll, small_ll):
#     ml(short_ll, small_ll)
#     assert small_ll.head.val == 5
#     assert small_ll.head._next.val == 1
#     assert small_ll.head._next._next._next._next._next._next._next.val == 4


# def test_merge_list_empty(short_ll, empty_ll):
#     assert ml(short_ll, empty_ll) == 5
#     assert len(short_ll) == 4


# def test_merge_list_empty_values(short_ll, empty_ll):
#     ml(short_ll, empty_ll)
#     assert short_ll.head.val == 5
#     assert short_ll.head._next.val == 6


# def test_merge_list_empty_first(empty_ll, short_ll):
#     assert ml(empty_ll, short_ll) == 5
#     assert len(short_ll) == 4


# def test_merge_list_empty_first_values(empty_ll, short_ll):
#     ml(empty_ll, short_ll)
#     assert short_ll.head.val == 5
#     assert short_ll.head._next.val == 6


def test_has_loop_false(small_ll):
    assert small_ll.has_loop() is False


def test_has_loop_true(small_ll):
    small_ll.head._next._next._next = small_ll.head
    assert small_ll.has_loop() is True


def test_has_loop_true_longer_and_not_head(long_ll):
    long_ll.head._next._next._next = long_ll.head._next
    assert long_ll.has_loop() is True


def test_has_loop_long_ll_false(long_ll):
    assert long_ll.has_loop() is False
