#!/usr/bin/env python3
"""
get  a list for those particular pagination parameters
"""

def index_range(page, page_size):
    """
    return a tuple of size two containing 
        a start index and an end index 
    """
    if page == 1:
        return (0, page_size)
    return (page_size * (page - 1), page * page_size)

res = index_range(1, 7)
print(type(res))
print(res)

res = index_range(page=3, page_size=15)
print(type(res))
print(res)