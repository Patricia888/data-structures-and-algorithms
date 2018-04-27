from functools import reduce


class HashTable:
    # allocated block of memory
    def __init__(self, max_size=1024):
        # each element should be a linked list
        self.max_size = max_size
        self.buckets = [None] * self.max_size

    def hash_key(self, key):
        if type(key) is not str:
            raise TypeError

        # expecting key to be a str
        # convert to unicode
            # iterate through key, and convert each char to ascii char code
        # add, divide by # of buckets
            # sum all char codes for a total int value
            # return => mod total by number of buckets
        # assign to bucket based on remainder

        sum = 0
        for char in key:
            # ord gets the integer value of each character
            sum += ord(char)
        return sum % self.buckets

        # return reduce(lambda a, b: a + ord(b), list(key), 0) % self.buckets

    def set(self, key, val):
        # hash the key, get a location for the bucket to insert into
        # DO LATER: traverse the linked list
        # set val into bucket

        # handle collisions
        # your vals may look something like a db record:
        #   {
            # 'id': '123',
            # 'name': 'xxx',    cat   act    => would cause a collision
            # 'title': 'zzz',
        # }

        # idx = self.hash_key(key)
        # self.buckets[idx] = value
        self.buckets[self.hash_key(key)] = val

    def get(self, key):
        return self.buckets[self.hash_key(key)]

    def remove(self, key):
        temp = self.buckets[self.hash_key(key)]
        self.buckets[self.hash_key(key)] = None
        return temp


# set, get, and remove should have access to linked list methods
# like get can use find
