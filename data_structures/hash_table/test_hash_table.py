import pytest
from .hash_table import HashTable
from .linked_list import LinkedList


def test_size_of_default_hashtable():
    """Test size of default hashtable."""
    h = HashTable()
    assert len(h.buckets) == 1024


def test_size_of_hashtable_size_10():
    """Test size of hashtable with a size of 10."""
    h = HashTable(10)
    assert len(h.buckets) == 10


def test_size_of_hashtable_invalid_arguments():
    """Test construction of hashtable with invalid size argument."""
    with pytest.raises(TypeError):
        HashTable('dog')


def test_hash_key_valid_input():
    """Test hash key method with valid input."""
    h = HashTable(10)
    assert h.hash_key('cat') == 2


def test_hash_key_valid_input_longer():
    """Test hash key method with a longer valid input."""
    h = HashTable(10)
    assert h.hash_key('califradulouspiexpialidocious') == 3


def test_hash_key_invalid_input():
    """Test hash key method with invalid input."""
    with pytest.raises(TypeError):
        h = HashTable(10)
        h.hash_key(47) == 2


def test_hash_set_with_valid_input():
    """Test hash set method with valid input."""
    h = HashTable(10)
    h.set('stl', 314)
    assert h.buckets[9].head.val == {'stl': 314}


def test_hash_set_with_collision():
    """Test hash set method with collision."""
    h = HashTable(10)
    h.set('nyl', 909)
    h.set('stl', 314)
    assert h.buckets[9].head.val == {'stl': 314}


def test_hash_set_with_invalid_input():
    """Test hash table set method with invalid input."""
    with pytest.raises(TypeError):
        h = HashTable(10)
        h.set(18, 314)


def test_get_method_with_valid_input():
    """Test get method with valid input."""
    h = HashTable(10)
    h.set('stl', 314)
    assert h.get('stl') == 314


def test_get_method_with_value_down_in_list():
    """Test get method with value buried in list."""
    h = HashTable(10)
    h.set('nyl', 909)
    h.set('stl', 314)
    assert h.get('nyl') == 909


def test_get_method_for_invalid_input():
    """Test get method with invalid input."""
    with pytest.raises(TypeError):
        h = HashTable(10)
        h.get(314)


def test_get_method_for_value_not_in_bucket():
    """Test get method with value not in list."""
    h = HashTable(10)
    assert h.get('stl') is False


def test_remove_method_with_valid_input():
    """Test remove method with valid input."""
    h = HashTable(10)
    h.set('stl', 314)
    assert h.remove('stl') == 314


def test_remove_method_with_value_down_in_list():
    """Test remove method with value buried in list."""
    h = HashTable(10)
    h.set('nyl', 909)
    h.set('stl', 314)
    assert h.remove('nyl') == 909
    assert h.buckets[9].head._next is None


def test_remove_all_method():
    """Test remove method with value buried in list."""
    h = HashTable(10)
    h.set('nyl', 909)
    h.set('stl', 314)
    h.remove('nyl', 'all')
    assert h.buckets[9].head is None


def test_remove_method_for_invalid_input():
    """Test remove method with invalid input."""
    with pytest.raises(TypeError):
        h = HashTable(10)
        h.remove(314)


def test_remove_method_for_no_input():
    """Test remove method with no input."""
    with pytest.raises(TypeError):
        h = HashTable(10)
        h.remove()


def test_remove_method_for_value_not_in_bucket():
    """Test remove method with value not in list."""
    h = HashTable(10)
    assert h.remove('stl') is False
