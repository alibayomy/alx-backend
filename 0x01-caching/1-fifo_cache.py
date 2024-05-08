#!/usr/bin/python3
"""BasicCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO Cache
    Store caching by FIFO algorithm
    """
    def __init__(self):
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        assgin item to the cache_dict, remove the
        first in if full
        """
        
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            keys_list = list(self.cache_data.keys())
            keys_list.sort()
            discard_item = keys_list[0]
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
my_cache = FIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()