#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
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

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Implement ypermedia pagination
        information.
        """
        self.dataset()
        self.indexed_dataset()

        assert index is None or (0 <= index <
                                 len(self.__indexed_dataset)), "Invalid index"

        start_idx = index if index is not None else 0
        end_idx = start_idx + page_size
        data = [self.__indexed_dataset[i] for i in range(start_idx, end_idx)
                if i in self.__indexed_dataset]

        next_index = end_idx if end_idx < len(
            self.__indexed_dataset) else None

        return {
            "index": start_idx,
            "data": data,
            "page_size": page_size,
            "next_index": next_index
        }
