#!/usr/bin/env python3
"""Module that defines a simple helper function for indexing."""
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
