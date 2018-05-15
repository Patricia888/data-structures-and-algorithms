import pytest


@pytest.fixture
def once_upon_a_time():
    """Return string."""
    return 'Once upon a time, there was a brave princess who...'


@pytest.fixture
def best_of_times():
    """Return string."""
    return 'It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...'


@pytest.fixture
def no_repeat_string():
    """Return string with no repeats."""
    return 'The last time I saw Richard it was Detroit in 68...'


@pytest.fixture
def empty_string():
    """Return string."""
    return ''
