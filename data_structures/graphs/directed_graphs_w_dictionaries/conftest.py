import pytest
from .directed_graph import find_path


dict_d_graph = {'A': ['B', 'C'],
                'B': ['C', 'D'],
                'C': ['D'],
                'D': ['C'],
                'E': ['F'],
                'F': ['C']}


@pytest.fixture
def empty_graph():
    return {}


@pytest.fixture
def basic_graph():
    return dict_d_graph
