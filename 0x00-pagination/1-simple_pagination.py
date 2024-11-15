#!/usr/bin/env python
""" Task 1: Pagination - Simple pagination """

import csv
import math
from typing import List

index_range = __import__('0-simple_helper_function').index_range


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
        """Return a page of data.
        """
        # try:
        #     # print(f'{page}: {page_size}')
        #     # page, page_size = page, page_size
        #     assert isinstance(page, int) and isinstance(page_size, int), \
        #         "page must be int"
        #
        #     page_number_size_tuple = index_range(page, page_size)
        #     start, end = page_number_size_tuple
        #     data = self.dataset()
        #     paginated_data = [data[i] for i in range(start, end)]
        #     return paginated_data
        #
        # except Exception as e:
        #     print(f"Error: {e}")
        #     return []
        assert isinstance(page, int) and isinstance(page_size, int), \
            "page must be int"
        assert page >= 0 and page_size > 0, \
            "page must be int"
        # assert page >= 0 and page_size > 0, \
        #     "page must be int"

        page_number_size_tuple = index_range(page, page_size)
        start, end = page_number_size_tuple
        data = self.dataset()
        # try:
        #     paginated_data = [data[i] for i in range(start, end)]
        # except Exception:
        #     paginated_data = []
        if len(data) >= end > start:
            paginated_data = [data[i] for i in range(start, end)]
        else:
            paginated_data = []

        return paginated_data
