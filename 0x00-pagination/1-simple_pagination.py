#!/usr/bin/env python3
"""
Simple pagination function
"""
import csv
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Get the cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """A method that gets the start and end index for pagination
        """
        nextPageStartIndex = page * page_size
        return nextPageStartIndex - page_size, nextPageStartIndex

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Getting the items for a given page number
        Args: page <int> - page number
            page_size <int> - number of items per page
        Returns: <List[List]> - a list of list(row)
                 when inputs are within range
                 ([]) - an empty list if parameters are out of range
        """
        assert type(page) == int and type(page_size) == int

        assert page > 0 and page_size > 0

        startIndex, endIndex = self.index_range(page, page_size)
        return self.dataset()[startIndex:endIndex]
