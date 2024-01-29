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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """method to return page data and associated data about dataset
        """
        page_number = page
        data = self.get_page(page, page_size)

        next_page = None
        if self.get_page(page + 1, page_size) != []:
            next_val = page
            next_page = next_val + 1
        prev_page = None
        if (page - 1) > 0 and self.get_page(page - 1, page_size) != []:
            prev_val = page
            prev_page = prev_val - 1

        total_pages = 0
        current_page = 1
        while True:
            c_page = self.get_page(current_page, page_size)
            if c_page != []:
                total_pages += 1
                current_page += 1
            else:
                break

        return {
            "page_size": len(data),
            "page": page_number,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
