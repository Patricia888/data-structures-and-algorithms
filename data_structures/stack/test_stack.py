import pytest
from .node import Node
from .stack import Stack


def test_make_invalid_stack():
    with pytest.raises(TypeError) as err:
        Stack(1)
    assert str(err.value) == 'Invalid iterable'


def test_make_invalid_node():
    with pytest.raises(TypeError) as err:
        Node(None)
    assert str(err.value) == 'Pass a value!!'


def test_make_valid_empty_stack(empty_stack):
    assert empty_stack.top is None
    assert len(empty_stack) == 0


def test_push_invalid(short_stack):
    assert short_stack.push(None).val == 5


def test_push_single_node(empty_stack):
    assert empty_stack.push(5).val == 5
    assert len(empty_stack) == 1


def test_push_many_node(empty_stack):
    assert empty_stack.push(3).val == 3
    assert empty_stack.push(12).val == 12
    assert len(empty_stack) == 2


def test_make_valid_stack(short_stack):
    assert short_stack.top.val == 5
    assert short_stack.top._next.val == 4
    assert len(short_stack) == 5


def test_make_valid_stack_tall(tall_stack):
    assert tall_stack.top.val == 10
    assert tall_stack.top._next.val == 9
    assert len(tall_stack) == 10


def test_pop(short_stack):
    assert short_stack.pop() == 5
    assert short_stack.top.val == 4
    assert len(short_stack) == 4


def test_pop_single(empty_stack):
    empty_stack.push(1)
    assert empty_stack.pop() == 1
    assert len(empty_stack) == 0


def test_pop_twice(tall_stack):
    tall_stack.pop()
    assert tall_stack.pop() == 9
    assert len(tall_stack) == 8


def test_peek(short_stack):
    assert short_stack.top.val == 5


def test_peek_long(tall_stack):
    assert tall_stack.top.val == 10


def test_peek_single(short_stack):
    short_stack.push(6)
    assert short_stack.top.val == 6
