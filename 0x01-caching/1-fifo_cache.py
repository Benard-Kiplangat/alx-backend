#!/usr/bin/env python3
"""A caching class that extends the Base_Caching class
   and implements the FIFO policy
"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A caching system FIFO policy: class FIFOCache extends the
       BaseCaching class and implements FIFO cache policy
    """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assigns items to the dictionary self.cache_data
        """

        if key is None or item is None:
            return

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item

    def get(self, key):
        """Return the value of key in self.cache_data
        """

        return self.cache_data.get(key, None)
