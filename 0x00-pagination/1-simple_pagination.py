# #!/usr/bin/env python3
import csv
import math
from typing import List


def index_range(page, page_size):
    """
    return a tuple of size two containing
        a start index and an end index
    """
    if page == 1:
        return (0, page_size)
    return (page_size * (page - 1), page * page_size)

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        documentation
        """
        assert page > 0
        assert page_size > 0
        start_end = index_range(page, page_size)
        return(self.dataset())
    
server = Server()

try:
    should_err = server.get_page(-10, 2)
except AssertionError:
    print("AssertionError raised with negative values")
print(server.get_page(1, 3))
print(server.get_page(3, 2))
print(server.get_page(3000, 100))