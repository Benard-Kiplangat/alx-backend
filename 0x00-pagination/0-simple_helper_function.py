#!/usr/bin/env python3
"""
A simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates start index and an end index corresponding to the range of
    indexes to return in a list

    attr: page <int> - the page number
          page_size <int> - the size of each page

    Return: Tuple of integers of size two
    """
    nextPageStartIndex = page * page_size
    return nextPageStartIndex - page_size, nextPageStartIndex
