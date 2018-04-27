from functools import reduce
from .linked_list import Node, LinkedList


class HashTable:
    # allocated block of memory
    def __init__(self, max_size=1024):
        # each element should be a linked list
        self.max_size = max_size
        self.buckets = [None] * self.max_size

    def hash_key(self, key):
        if type(key) is not str:
            raise TypeError

        sum = 0
        for char in key:
            # ord gets the integer value of each character
            sum += ord(char)
        return sum % self.buckets

    def set(self, key, val):
        # DO LATER: traverse the linked list
        # set val into bucket

        # handle collisions
        # your vals may look something like a db record:
        #   {
            # 'id': '123',
            # 'name': 'xxx',    cat   act    => would cause a collision
            # 'title': 'zzz',
        # }


        # if no value is in that particular bucket, no worries about collisions
        if self.buckets is None:
            self.buckets[self.hash_key(key)] = val

        else:
            # create a linked list for the bucket to deal with collisions

    def get(self, key):
        return self.buckets[self.hash_key(key)]

    def remove(self, key):
        temp = self.buckets[self.hash_key(key)]
        self.buckets[self.hash_key(key)] = None
        return temp


# set, get, and remove should have access to linked list methods
# like get can use find
