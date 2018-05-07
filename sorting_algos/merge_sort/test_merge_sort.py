import pytest
from .merge_sort import merge_sort_the_list


def test_merge_sort_the_list_example_sort():
    ''' Test that the merge sort function sorts the unsorted example list. '''
    example_list = [34, 19, 42, -9, 2018, 0, 2005, 77, 2099]
    assert merge_sort_the_list(example_list) == [-9, 0, 19, 34, 42, 77, 2005, 2018, 2099]


def test_merge_sort_the_list_one_value_in_list():
    '''Test that it just returns the same thing put in when list length is 1.'''
    one_value_list = [5]
    assert merge_sort_the_list(one_value_list) == [5]


def test_merge_sort_the_list_reverse_sorted_list():
    '''Test that it sorts a list that is sorted in reverse'''
    reverse_sorted_list = [19, 6, 5, 4, 3, 1]
    assert merge_sort_the_list(reverse_sorted_list) == [1, 3, 4, 5, 6, 19]


def test_merge_sort_the_list_all_negative_values():
    '''Test that it sorts properly when all values in list are negative.'''
    negative_value_list = [-5, -20, -70, -1, -4]
    assert merge_sort_the_list(negative_value_list) == [-70, -20, -5, -4, -1]
