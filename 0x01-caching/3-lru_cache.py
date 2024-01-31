#!/usr/bin/python3
"""
This module creates a class LRUCache that inherits from
BaseCaching and is a caching system that implements LRU
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """A class for LRU caching."""

    def put(self, key, item):
        """
        Add an item to the lifo queue cache. ensuring
        most recent item is always at the end of the
        cache

        Args:
            key (hashable): The key of the item.
            item: The value to add to the cache.

        Returns:
            None
        """
        # Note ordering in a dictionary is maintained
        # only from python version 3.7 onward hence
        # this code will behave differently in low vs.
        if key is not None and item is not None:
            stack = self.cache_data
            if len(stack) == BaseCaching.MAX_ITEMS:
                if key not in stack:
                    first_key = list(stack.keys())[0]
                    stack.pop(first_key)
                    print(f'DISCARD: {first_key}')
                else:
                    del stack[key]
            stack[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache but move it to
        the end of the cache making it MRU before retrieval

        Args:
            key (hashable): The key of the item to retrieve.

        Returns:
            The retrieved item, or None if not present.
        """
        if self.cache_data.get(key, None):
            # operations to move item to end making it
            # most recently used
            value = self.cache_data[key]
            del self.cache_data[key]
            self.cache_data[key] = value
        return self.cache_data.get(key, None)
