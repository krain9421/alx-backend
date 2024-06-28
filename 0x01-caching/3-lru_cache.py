#!/usr/bin/env python3
"""
Module that defines a class that inherits from BaseCaching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class that is a caching system
    LRUCache uses Least Recently Used cache method
    """
    def __init__(self):
        """
        Init method
        """
        super().__init__()
        self.lrused = {}
        self.count = 0

    def put(self, key, item):
        """
        Method that adds an item by key
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data:
                print(f"DISCARD: {lru}")
                lrukey = self.get_lrukey()
                del self.cache_data[lrukey]
                del self.used[lrukey]
        self.cache_data[key] = item
        self.lrused[key] = count++

    def get(self, key):
        """
        Method that gets an item by key
        """
        if key is None:
            return None
        return self.cache_data.get(key)

    def get_lrukey(self):
        """
        Method that returns the key of the
        least recently used item
        """
        lru = list(self.lrused.values())[0]
        lrukey = list(self.lrused.keys())[0]
        for k, v in self.lrused:
            if v < lru:
                lrukey = k
        return lrukey
