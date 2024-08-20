#!/usr/bin/env python3
"""Basic caching class that extends the Base_Caching class
"""

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """A caching system: class BasicCache extends the
       BaseCaching class
    """

    def put(self, key, item):
        """Assigns items to the dictionary self.cache_data
        """

        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Return the value of key in self.cache_data
        """

        return self.cache_data.get(key, None)
