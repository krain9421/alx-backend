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
    # end_index = start_index + page_size
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
        """
        Function that takes an index ranged and returns a paginated dataset
        """
        # Verify that both arguments are non-zero integers
        assert isinstance(page, int) and page > 0, "Error"
        assert isinstance(page_size, int) and page_size > 0, "Error"

        # Get the index range and start/end indexes
        page_range = index_range(page, page_size)
        start = page_range[0]
        end = page_range[1]

        dataset_n = self.dataset()
        if (end - start >= len(dataset_n)):
            result = []
        else:
            result = dataset_n[start: end]
        return result
