#!/usr/bin/env python3
"""Task 0: Basic dictionary"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Child Class that inherits from Parent Class BaseCaching"""
    def __int__(self):
        super().__init__()

    def put(self, key, item):
        """ Attach key value pair to cache dict"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Return item value """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
