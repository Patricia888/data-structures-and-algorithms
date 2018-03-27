from .shift_array import insertShiftArray
import pytest


def test_insertShiftArray_odd():
    assert insertShiftArray([1,2,3,4,5,6,7,8,9], 'X') == [1, 2, 3, 4, 'X', 5, 6, 7, 8, 9]


def test_insertShiftArray_with_even():
    assert insertShiftArray([1,2,3,4,5,6,7,8], 'X') == [1, 2, 3, 4, 'X', 5, 6, 7, 8]


def test_insertShiftArray_with_empty():
    assert insertShiftArray([], 'X') == ['X']
