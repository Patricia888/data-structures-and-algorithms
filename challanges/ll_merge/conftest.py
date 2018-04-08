import pytest
from .ll_merge import LinkedList as LL


@pytest.fixture
def empty_ll():
    return LL()


@pytest.fixture
def small_ll():
    return LL([1, 2, 3, 4])


@pytest.fixture
def short_ll():
    return LL([5, 6, 7, 8])


@pytest.fixture
def long_ll():
    return LL([11, 12, 13, 14, 15, 16])
