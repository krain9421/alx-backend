#!/usr/bin/env python3
"""
Module that defines a class that inherits from BaseCaching
"""
from base_caching import BaseCaching
from datetime import datetime
import math


class MRUCache(BaseCaching):
    """
    MRUCache class that is a caching system
    MRUCache uses Most Recently Used cache method
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
                lrukey = self.get_lrukey()
                print(f"DISCARD: {lrukey}")
                del self.cache_data[lrukey]
                del self.lrused[lrukey]
        self.cache_data[key] = item
        # self.lrused[key] = self.count = self.count + 1
        self.lrused[key] = datetime.now()

    def get(self, key):
        """
        Method that gets an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        if key in self.cache_data:
            self.lrused[key] = datetime.now()
        return self.cache_data.get(key)

    def get_lrukey(self):
        """
        Method that returns the key of the
        least recently used item
        """
        lru = list(self.lrused.values())[0]
        lrukey = list(self.lrused.keys())[0]
        for k, v in self.lrused.items():
            if v > lru:
                lrukey = k
        return lrukey
