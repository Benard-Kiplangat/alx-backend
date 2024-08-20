#!/usr/bin/env python3
"""A caching class that extends the Base_Caching class
   and implements the LRU caching policy
"""
from collections import OrderedDict
from base_caching import BaseCaching

class LRUCache(BaseCaching):
    """A caching system LRU policy: class LRUCache extends the
       BaseCaching class and implements LRU cache policy
    """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assigns items to the dictionary self.cache_data
        """

        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Return the value of key in self.cache_data
        """

        return self.cache_data.get(key, None)
