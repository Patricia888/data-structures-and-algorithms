import pytest
from . import AnimalShelter


@pytest.fixture
def empty_queue():
    return AnimalShelter()


@pytest.fixture
def short_queue():
    return AnimalShelter(['dog', 'cat', 'dog', 'cat'])


@pytest.fixture
def ddc_queue():
    return AnimalShelter(['dog', 'dog', 'cat'])
