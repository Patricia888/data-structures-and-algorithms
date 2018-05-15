from .hash_table import HashTable


def repeated_word(lengthy_string):
    """Return the first repeated word of an lengthy input string."""
    lengthy_string = lengthy_string.lower()
    lengthy_list = lengthy_string.split(' ')
    ht = HashTable(len(lengthy_list))
    for word in lengthy_list:
        if ht.get(word):
            return word
        else:
            ht.set(word, word)
    return False
