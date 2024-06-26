#!/usr/bin/env python3
"""
Module that defines a class that inherits from BaseCaching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class that is a caching system
    """
    def put(self, key, item):
        """
        Method that adds an item by key
        Method adds item to cache by FIFO method
        """
        if key is None or item is None:
            return
        #  Check if cache is full
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data:
                first = list(self.cache_data.keys())[0]
                print(f"DISCARD: {first}")
                del self.cache_data[first]
        self.cache_data[key] = item

    def get(self, key):
        """
        Method that gets an item by key
        """
        if key is None:
            return None
        return self.cache_data.get(key)
