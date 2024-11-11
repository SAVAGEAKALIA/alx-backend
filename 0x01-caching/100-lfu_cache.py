#!/usr/bin/env python3
"""
Task 5. LFU Caching Less Frequently used
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Class for LFU caching
    Inherits from BaseCaching class
    """
    def __init__(self):
        """
        Initialize the LFUCache class.
        Inherits From parent Class
        """
        super().__init__()
        self.frequency = {}  # To track the frequency of keys
        self.access_order = {}  # To track the access order of keys

    def put(self, key, item):
        """
        Add an item in the cache while checking Frequency
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the item and its frequency
            self.cache_data[key] = item
            self.frequency[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used key
                lfu_keys = [k for k, v in self.frequency.items() if v == min(self.frequency.values())]
                if len(lfu_keys) > 1:
                    # If there is a tie, use the least recently used key
                    lfu_key = min(lfu_keys, key=lambda k: self.access_order[k])
                else:
                    lfu_key = lfu_keys[0]

                # Discard the LFU (or LRU) key
                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                del self.access_order[lfu_key]
                print(f"DISCARD: {lfu_key}")

            # Add the new item and set its frequency to 1
            self.cache_data[key] = item
            self.frequency[key] = 1

        # Update the access order
        self.access_order[key] = len(self.access_order)

    def get(self, key):
        """
        Retrieve Item an item by key.
        """
        if key is None or key not in self.cache_data:
            return None
        # Update the frequency and access order
        self.frequency[key] += 1
        self.access_order[key] = len(self.access_order)
        return self.cache_data[key]
