#!/usr/bin/env python3
"""
Module that defines a class that inherits from BaseCaching
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that is a caching system
    """
    def put(self, key, item):
        """
        Method that adds an item by key
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Method that gets an item by key
        """
        if key is None:
            return None
        return self.cache_data.get(key)
