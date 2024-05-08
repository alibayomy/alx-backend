#!/usr/bin/python3
"""LIFOCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO Cache
    Store caching by LIFO algorithm
    """
    def __init__(self):
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        assgin item to the cache_dict, remove the
        first in if full
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            keys_list = list(self.cache_data.keys())
            keys_list.sort()
            discard_item = keys_list[-1]
            del self.cache_data[discard_item]
            print(f'DISCARD: {discard_item}')
        self.cache_data[key] = item

    def get(self, key):
        """
        Return the value of cache dict based on
            the given key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
