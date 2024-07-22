#!/usr/bin/env python3
"""Python module that implements simple pagination."""
import csv
import math
from typing import List, Set, Dict, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Function takes two integer arguments and returns a tuple
        of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list
        for those particular pagination parameters.
    """
    start_index = page_size * (page - 1)
    end_index = page_size * page
    return (start_index, end_index)


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
        # Verify that both arguments are non-zero integers
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page_size > 0 and page > 0

        # Get the index range
        page_range = index_range(page, page_size)

        dataset_n = self.dataset()
        if (page_range[0] >= len(dataset_n) or page_range[1] >= len(dataset_n)):
            result = []
        else:
            result = dataset_n[page_range[0]: page_range[1]]
        return result
