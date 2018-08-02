import pytest
from .directed_graph import find_path


def test_empty_dict(empty_graph):
    assert find_path(empty_graph, 'A', 'D') is None


def test_basic_graph_basic_path(basic_graph):
    assert find_path(basic_graph, 'A', 'D') == ['A', 'B', 'C', 'D']
