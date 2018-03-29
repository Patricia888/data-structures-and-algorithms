import pytest
from linked_list import LinkedList as LL
# from snakes_cafe import snakescafe as sc


@pytest.fixture
def empty_ll():
    return LL()


@pytest.fixture
def small_ll():
    return LL([1, 2, 3, 4])
