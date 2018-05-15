import pytest
from .hash_table import HashTable

@pytest.fixture
def hash_table_empty_size_ten():
    """Create hash table with 10 buckets."""
    return HashTable(10)


@pytest.fixture
def hash_table_two_vals_one_bucket():
    """Create hash table with 10 buckets."""
    h = HashTable(10)
    h.set('nyl', 909)
    h.set('stl', 314)
    return h
