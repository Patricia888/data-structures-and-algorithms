import shift-array
import pytest


def test_insertShiftArray_odd():
    assert shift-array.insertShiftArray([1,2,3,4,5,6,7,8,9], 'X') == [1, 2, 3, 4, 'X', 5, 6, 7, 8, 9]


def test_insertShiftArray_with_even():
    assert shift-array.insertShiftArray([1,2,3,4,5,6,7,8], 'X') == [1, 2, 3, 4, 'X', 5, 6, 7, 8]


def test_insertShiftArray_with_empty():
    assert shift-array.insertShiftArray([], 'X') == ['X']