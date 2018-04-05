import pytest
from .multi_bracket_validation import multi_bracket_validation


def test_raises_error():
    with pytest.raises(ValueError):
        multi_bracket_validation(7)


def test_simple_true():
    assert multi_bracket_validation('()') == True


def test_simple_false():
    assert multi_bracket_validation('{[)') == False


def test_gives_true_positive():
    assert multi_bracket_validation('{[]}([)]') == True


def test_gives_true_negative():
    assert multi_bracket_validation('){}[]([') == False
