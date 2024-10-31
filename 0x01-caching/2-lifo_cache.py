#!/usr/bin/env python3
"""A caching class that extends the Base_Caching class
   and implements the LIFO policy
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A caching system LIFO policy: class LIFOCache extends the
       BaseCaching class and implements LIFO cache policy
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
                last_key, _ = self.cache_data.popitem(last=True)
                print(f"DISCARD: {last_key}")

        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Return the value of key in self.cache_data
        """

        return self.cache_data.get(key, None)
