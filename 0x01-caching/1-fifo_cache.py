#!/usr/bin/env python
"""Task 1: FIFO Caching"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Class for FIFO caching First in First out"""

    def __init__(self):
        """Inherit from BaseCaching"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Put a key/value pair into the cache"""
        if key in self.cache_data:
            self.cache_data[key] = item
        elif key is None or item is None:
            return
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.queue = [value for value in self.cache_data.keys()]
                old_key = self.queue[0]
                del self.cache_data[old_key]
                self.queue.clear()
                print(f'DISCARD: {old_key}')
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        """ Return item value """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
