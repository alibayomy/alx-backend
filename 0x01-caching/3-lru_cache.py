#!/usr/bin/python3
"""LRUCache  module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRU Cache
    Store caching by LRU algorithm
    """
    def __init__(self):
        BaseCaching.__init__(self)
        self.keys_list = []

    def put(self, key, item):
        """
        assgin item to the cache_dict, remove the
        the least recently used in if full
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key in self.cache_data.keys():
                self.keys_list.remove(key)
                self.cache_data[key] = item
            else:
                discard_item = self.keys_list[0]
                del self.cache_data[discard_item]
                self.keys_list.remove(discard_item)
                print(f'DISCARD: {discard_item}')
        self.keys_list.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Return the value of cache dict based on
            the given key and update the key_list
            to record the least recently used
        """
        if key is None or key not in self.cache_data.keys():
            return None
        if key in self.keys_list:
            self.keys_list.remove(key)
        self.keys_list.append(key)
        return self.cache_data[key]
