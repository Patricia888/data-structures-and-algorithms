import pytest
from .ll_merge import LinkedList as LL


@pytest.fixture
def empty_ll():
    return LL()


@pytest.fixture
def small_ll():
    return LL([1, 2, 3, 4])


@pytest.fixture
def merge_small_ll():
    return LL([8, 9, 10, 11])


@pytest.fixture
def merge_long_ll():
    return LL([12, 13, 14, 15, 16, 167])
