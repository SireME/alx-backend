#!/usr/bin/env python3
"""
This module contains a Simple pagination implementation using
previously implemented helper function index_range
"""
import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int]:
    """ formular to compute strat index and end index for pagination"""
    start_index = (page - 1) * page_size
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
        """"This method retrives a page of data from dataset
        """
        self.dataset()  # ensure data is always loaded
        try:
            assert page > 0, "page should be greater than Zero(0)"
            assert page_size > 0, "page_size should be greater than 0"
        except TypeError:
            assert not TypeError

        indexes = index_range(page, page_size)

        data = []

        try:
            for i in range(indexes[0], indexes[1]):
                data.append(self.__dataset[i])
        except IndexError:
            pass

        return data
