#!/usr/bin/python3
"""
This module creates a class BasicCache that inherits from
 BaseCaching and is a caching system
 """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class for basic caching"""
    def put(self, key, item):
        """method to add item to cache
        Args:
            key: key of value to add to cache
            value: value to add to cache
        Return: None
        """
        if None not in (key, item):
            self.cache_data[key] = item

    def get(self, key):
        """
        method to retrieve itme from cache
        Args:
            key: key of item to retrieve
        Return:
            retrieved item or None if not present
         """
        return self.cache_data.get(key, None)
