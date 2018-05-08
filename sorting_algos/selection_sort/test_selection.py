import pytest
from .selection import selection_sort


def test_selection_sort_example_from_merge_sort():
    ''' Test that the merge sort function sorts the unsorted example list. '''
    example_list = [34, 19, 42, -9, 2018, 0, 2005, 77, 2099]
    assert selection_sort(example_list) == [-9, 0, 19, 34, 42, 77, 2005, 2018, 2099]


def test_selection_sort_one_value_in_list():
    '''Test that it just returns the same thing put in when list length is 1.'''
    one_value_list = [5]
    assert selection_sort(one_value_list) == [5]


def test_selection_sort_reverse_sorted_list():
    '''Test that it sorts a list that is sorted in reverse'''
    reverse_sorted_list = [19, 6, 5, 4, 3, 1]
    assert selection_sort(reverse_sorted_list) == [1, 3, 4, 5, 6, 19]


def test_selection_sort_all_negative_values():
    '''Test that it sorts properly when all values in list are negative.'''
    negative_value_list = [-5, -20, -70, -1, -4]
    assert selection_sort(negative_value_list) == [-70, -20, -5, -4, -1]


def test_selection_sort_repeat_numbers_in_list():
    ''' Tests it properly sorts when the inputted list has repeat values'''
    repeat_number_list = [4, 4, 2, 9, 9, 4, 2, 1]
    assert selection_sort(repeat_number_list) == [1, 2, 2, 4, 4, 4, 9, 9]
