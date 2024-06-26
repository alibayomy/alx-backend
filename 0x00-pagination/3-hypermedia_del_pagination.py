#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        return a dictionary with the  key-value pairs
        """
        indexed_len = len(self.__indexed_dataset)
        assert isinstance(index, int) and isinstance(page_size, int)
        assert index > 0 and page_size > 0 and index is not None
        assert index <= len(self.__indexed_dataset)
        last_index = index + page_size
        last_index = None if last_index > len(indexed_len) else last_index
        data = []
        i = index
        while i < last_index:
            try:
                data.append(self.__indexed_dataset[i])
            except KeyError:
                last_index = last_index + 1
            i += 1
        next_index = last_index
        return({
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index
        })
