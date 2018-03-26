import pytest
import linked_list


@pytest.fixture
def empty_linked_list():
    return linked_list()
