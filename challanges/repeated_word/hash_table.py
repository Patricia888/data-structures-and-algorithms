from .linked_list import LinkedList


class HashTable:
    """Hash table class."""
    def __init__(self, max_size=1024):
        if type(max_size) is not int:
            raise TypeError
        self.max_size = max_size
        self.buckets = [LinkedList()] * self.max_size

    def hash_key(self, key):
        """Hash key."""
        if type(key) is not str:
            raise TypeError
        
        sum = 0
        for char in key:
            sum += ord(char)
        return sum % len(self.buckets)

    def set(self, key, val):
        """Set new value in hash table."""
        if type(key) is not str:
            raise TypeError

        self.buckets[self.hash_key(key)].insert({key: val})
        self.buckets[self.hash_key(key)]._size += 1

    def get(self, key):
        """Get value in hash table."""
        if type(key) is not str:
            raise TypeError

        current = self.buckets[self.hash_key(key)].head
        while current:
            if key in current.val:
                return current.val[key]
            current = current._next

        print('The key {} is not in this hash table'.format(key))
        return False

    def remove(self, key='', all_or_none=None):
        """
        Remove value in hash table.
        If user specifies 'all' in all_or_none, entire linked list will
        be emptied.
        """
        if type(key) is not str:
            raise TypeError
        
        if key == '':
            print('To remove value or enite bucket, a value must be given')
            raise TypeError
        
        if all_or_none == 'all':
            self.buckets[self.hash_key(key)].head = None

        current = self.buckets[self.hash_key(key)].head
        previous = None
        while current:
            if key in current.val:
                if previous is None:
                    self.buckets[self.hash_key(key)].head = current._next
                    return current.val[key]
                else:
                    previous._next = current._next
                    return current.val[key]
            previous = current
            current = current._next
        print('The key {} is not in this hash table'.format(key))
        return False
