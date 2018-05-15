from .hash_table import HashTable
import pytest
from .repeated_word import repeated_word


def test_repeated_word_short_string(once_upon_a_time):
    """Test for expected result of 'a'."""
    assert repeated_word(once_upon_a_time) == 'a'


def test_repeate_word_long_string(best_of_times):
    """Test for expected result 'the' on lengthy string."""
    assert repeated_word(best_of_times) == 'it'


def test_repeated_word_no_repeats(no_repeat_string):
    """Test for expected result of False."""
    assert repeated_word(no_repeat_string) is False


def test_repeated_word_func_empty_string(empty_string):
    """Test for expected result False in empty string."""
    assert repeated_word(empty_string) is False
