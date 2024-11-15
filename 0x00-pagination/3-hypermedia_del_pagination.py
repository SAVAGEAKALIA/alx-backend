#!/usr/bin/env python3
""" Task 3: Pagination - Deletion-resilient hypermedia pagination"""

import csv
import math
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialization insatance of the server"""
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

    def get_hyper_index(self, index: int = None, page_size: int = 10) \
            -> Dict[str, Any]:
        """returns a dictionary containing the following key-value pairs:

            index: the index of the dataset item
            data: the dataset item at the given index
            page_size: the length of the returned dataset page"""

        indexed_data = self.indexed_dataset()
        assert 0 <= index < len(indexed_data), \
            "Index out of range"

        next_index = index
        collected_count = 0

        data_proper = []
        # for i in range(page_size):
        #     if i in indexed_data:
        #         data_proper.append(indexed_data[i])
        #         collected_count += 1
        #         next_index += 1
        #     else:
        #         next_index += 1
        #         break

        while collected_count < page_size and next_index < len(indexed_data):
            if next_index in indexed_data:  # Check if the row exists
                data_proper.append(indexed_data[next_index])
                collected_count += 1
            next_index += 1

        to_dict = {
            "index": index,
            "data": data_proper,
            "page_size": page_size,
            "next_index":
                next_index if next_index < len(indexed_data) else None,
        }
        return to_dict
