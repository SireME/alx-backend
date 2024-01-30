#!/usr/bin/python3
"""
This module creates a class FIFOCache that inherits from
BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A class for fifo caching."""

    def put(self, key, item):
        """
        Add an item to the fifo stack cache.

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
                first_key = list(stack.keys())[0]
                stack.pop(first_key)
                print(f'DISCARD: {first_key}')
            stack[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key (hashable): The key of the item to retrieve.

        Returns:
            The retrieved item, or None if not present.
        """
        return self.cache_data.get(key, None)
