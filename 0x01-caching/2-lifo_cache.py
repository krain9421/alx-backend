#!/usr/bin/env python3
"""
Module that defines a class that inherits from BaseCaching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that is a caching system
    LIFOCache uses LIFO cache method
    """
    def __init__(self):
        """
        Init method
        """
        super().__init__()
        self.last = None

    def put(self, key, item):
        """
        Method that adds an item by key
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data:
                print(f"DISCARD: {self.last}")
                del self.cache_data[self.last]
        self.cache_data[key] = item
        self.last = key

    def get(self, key):
        """
        Method that gets an item by key
        """
        if key is None:
            return None
        return self.cache_data.get(key)
