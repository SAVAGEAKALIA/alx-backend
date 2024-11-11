#!/usr/bin/env python3
"""Task 0: Basic dictionary"""

from BaseCaching import BaseCaching


class BasicCache(BaseCaching):
    """Child Class that inherits from Parent Class BaseCaching"""
    def __int__(self, cache_data):
        super().__init__(cache_data)

    def put(self, key, item):
        """ Attach key value pair to cache dict"""
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """ Return item value """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
