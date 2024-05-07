#!/usr/bin/python3
"""BasicCache module
"""
BaseCaching  = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """ BasicCache defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    def __init__(self):
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        Assging to the cache dict the key and the item
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Return the value of cache dict based on
            the given key
            """
        if key is None  or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
    
my_cache = BasicCache()
my_cache.print_cache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
print(my_cache.get("D"))
my_cache.print_cache()
my_cache.put("D", "School")
my_cache.put("E", "Battery")
my_cache.put("A", "Street")
my_cache.print_cache()
print(my_cache.get("A"))