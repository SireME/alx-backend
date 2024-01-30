#!/usr/bin/python3
"""
This module creates a class BasicCache that inherits from
BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A class for basic caching."""

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key (hashable): The key of the item.
            item: The value to add to the cache.

        Returns:
            None
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key (hashable): The key of the item to retrieve.

        Returns:
            The retrieved item, or None if not present.
        """
        return self.cache_data.get(key, None)
