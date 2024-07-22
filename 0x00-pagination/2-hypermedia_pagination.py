#!/usr/bin/env python3
"""Python module that implements simple hypermedia pagination"""
import csv
import math
from typing import List, Set, Dict, Tuple, Union, Optional


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Function takes two integer arguments and returns a tuple
        of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list
        for those particular pagination parameters.
    """
    start_index = page_size * (page - 1)
    # end_index = page_size * page
    end_index = start_index + page_size
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Function that returns a dictionary
        that contains info on a paginated dataset

        Dict[str, Union[int, List[List], Optional[int]]]
        # Verify that both arguments are non-zero integers
        assert isinstance(page, int) and page > 0, "Error"
        assert isinstance(page_size, int) and page_size > 0, "Error"

        # Get the index range and start/end indexes
        page_range = index_range(page, page_size)
        start = page_range[0]
        end = page_range[1]

        dataset_n = self.dataset()
        if (end - start >= len(dataset_n)):
            dataset_f = []
        else:
            dataset_f = dataset_n[start: end]
        """
        # Get data for the dictionary
        result = {}
        dataset_n = self.dataset()
        dataset_f = self.get_page(page, page_size)

        result['page_size'] = len(dataset_f)
        result['page'] = page
        result['data'] = dataset_f
        if(page * page_size >= len(dataset_n)):
            result['next_page'] = None
        else:
            result['next_page'] = page + 1
        if((page - 1) * page_size <= 0):
            result['prev_page'] = None
        else:
            result['prev_page'] = page - 1
        if (len(dataset_n) % page_size > 0):
            total_p = len(dataset_n) // page_size
            result['total_pages'] = total_p + 1
        else:
            result['total_pages'] = len(dataset_n) // page_size

        return result
