#!/usr/bin/env python3
""" Task 2: Pagination - Hypermedia pagination """

import csv
import math
from typing import List, Dict, Any

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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """returns a dictionary containing the following key-value pairs:

            page_size: the length of the returned dataset page
            page: the current page number
            data: the dataset page (equivalent to return from previous task)
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: the total number of pages in the dataset as an integer
        """

        data = self.dataset()
        data_set_get_page = self.get_page(page, page_size)
        # current_page, current_page_size = index_range(page, page_size)
        total_pages = math.ceil(len(data) / page_size)
        # next_page = current_page + 1
        # previous_page = current_page - 1

        # print(data_set_get_page)

        next_page = page + 1 if page < total_pages else None
        # prev_page = page - 1 if page > 1 else None
        if page > 1:
            prev_page = page - 1
            if total_pages < page:
                page_size = 0
        else:
            prev_page = None

        to_dict = {
            "page_size": None,
            "page": None,
            "data": None,
            "next_page": None,
            "prev_page": None,
            "total_pages": None
        }

        for key in to_dict.keys():
            if key == "page_size":
                to_dict[key] = page_size
            elif key == "page":
                to_dict[key] = page
            elif key == "data":
                to_dict[key] = data_set_get_page
            elif key == "next_page":
                to_dict[key] = next_page
            elif key == "prev_page":
                to_dict[key] = prev_page
            else:
                to_dict[key] = total_pages

        # print(to_dict)
        return to_dict