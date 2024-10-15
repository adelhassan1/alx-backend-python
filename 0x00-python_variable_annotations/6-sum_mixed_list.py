#!/usr/bin/env python3
"""
Mixed list
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list of integers and floats and returns their sum as float.
    """
    return sum(mxd_lst)
