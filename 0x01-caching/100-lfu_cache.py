#!/usr/bin/python3
"""
This module creates a class LFUCache that inherits from
BaseCaching and is a caching system that implements LFU
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFU cache implementation """

    def __init__(self):
        """ Initialize LFUCache """
        super().__init__()
        self.frequency = {}
        self.lfu_count = {}

    def put(self, key, item):
        """ Add an item to the cache using LFU algorithm """

        if key is None or item is None:
            return

        # If cache is at max capacity, discard the least frequently used item
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lfu_items = []
            for k, v in self.frequency.items():
                if v == min(self.frequency.values()):
                    lfu_items.append(k)
            lru_item = min(lfu_items, key=lambda k: self.lfu_count.get(k, 0))
            del self.cache_data[lru_item]
            del self.frequency[lru_item]
            print("DISCARD:", lru_item)

        # Update cache with new item
        self.cache_data[key] = item

        # Update frequency count for the key
        self.frequency[key] = self.frequency.get(key, 0) + 1

        # Update LFU count for the key
        self.lfu_count[key] = 0

    def get(self, key):
        """ Get an item from the cache using LFU algorithm """
        if key is None or key not in self.cache_data:
            return None

        # Increment LFU count for the key
        self.lfu_count[key] += 1

        # Return the value associated with the key
        return self.cache_data[key]
