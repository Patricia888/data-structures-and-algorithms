from . import AnimalShelter
import pytest


def test_empty_shelter(empty_queue):
    assert empty_queue.front is None
    assert empty_queue.back is None
    assert empty_queue._size == 0


def test_make_invalid_queue():
    with pytest.raises(TypeError) as err:
        AnimalShelter(1)
    assert str(err.value) == 'Invalid iterable'


def test_enqueue_invalid(short_queue):
    with pytest.raises(ValueError):
        short_queue.enqueue(None)


def test_dequeue_invalid(empty_queue):
    with pytest.raises(IndexError) as err:
        empty_queue.dequeue()
    assert str(err.value) == 'animal shelter is empty'


def test_enqueue_invalid_animal(short_queue):
    with pytest.raises(ValueError):
        short_queue.enqueue('turtle')


def test_dequeue_invalid_animal(ddc_queue):
    with pytest.raises(TypeError):
        ddc_queue.dequeue(1)


def test_instantiate_with_iterable():
    animals = AnimalShelter(['dog', 'dog', 'cat'])
    assert animals._size == 3
    assert animals.front.val == 'dog'
    assert animals.back.val == 'cat'


def test_enqueue_dog(empty_queue):
    empty_queue.enqueue('dog')
    assert empty_queue.front.val == 'dog'
    assert empty_queue._size == 1


def test_enqueue_cat(empty_queue):
    empty_queue.enqueue('cat')
    assert empty_queue.front.val == 'cat'
    assert empty_queue._size == 1


def test_enqueue_twice(empty_queue):
    empty_queue.enqueue('dog')
    empty_queue.enqueue('cat')
    assert empty_queue._size == 2
    assert empty_queue.front.val == 'dog'


def test_dequeue_none(short_queue):
    assert short_queue.dequeue() == 'dog'
    assert short_queue.front.val == 'cat'


def test_dequeue_dog(short_queue):
    assert short_queue.dequeue('dog') == 'dog'
    assert short_queue.front.val == 'cat'
    assert short_queue._size == 3


def test_dequeue_cat(short_queue):
    assert short_queue.dequeue('cat') == 'cat'
    assert short_queue._size == 3
    assert short_queue.front.val == 'dog'


def test_dequeue_cat_vals(short_queue):
    short_queue.dequeue('cat')
    assert short_queue.front._next.val == 'dog'
    assert short_queue.front._next._next.val == 'cat'


def test_dequeue_cat_ddc(ddc_queue):
    assert ddc_queue.dequeue('cat') == 'cat'
    assert ddc_queue._size == 2


def test_dequeue_cat_ddc_vals(ddc_queue):
    ddc_queue.dequeue('cat')
    assert ddc_queue.front.val == 'dog'
    assert ddc_queue.front._next.val == 'dog'


def test_dequeue_dog_ddc(ddc_queue):
    assert ddc_queue.dequeue('dog') == 'dog'
    assert ddc_queue.front.val == 'dog'
    assert ddc_queue._size == 2


def test_dequeue_not_dog_or_cat(ddc_queue):
    with pytest.raises(ValueError):
        ddc_queue.dequeue('wolf')
