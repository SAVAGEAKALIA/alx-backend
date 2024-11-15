#!/usr/bin/env python
""" Task 0: Pagination Return a Tuple """
from typing import Tuple


def index_range(page: int = None, page_size: int = None) -> Tuple[int, int]:
    """Function to return a Tuple"""
    start = (page - 1) * page_size
    end = page * page_size
    return start, end
