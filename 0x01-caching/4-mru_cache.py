#!/usr/bin/env python3
"""Task 1: MRU Caching"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Class for LIFO caching First in First out"""

    def __init__(self):
        """Inherit from BaseCaching"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Put a key/value pair into the cache"""
        if key in self.cache_data:
            # temp_store = self.cache_data[key]
            self.cache_data.pop(key)
            self.cache_data[key] = item
        elif key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.queue = [value for value in self.cache_data.keys()]
                last_key_in = self.queue[-1]
                del self.cache_data[last_key_in]
                self.queue.clear()
                print(f'DISCARD: {last_key_in}')
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        """ Return item value"""
        if key is None or key not in self.cache_data:
            return None
        temp_store = self.cache_data.pop(key)
        self.cache_data[key] = temp_store
        return self.cache_data.get(key)
