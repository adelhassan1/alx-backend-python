#!/usr/bin/env python3
"""
Iterable object
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returning values with the appropriate types.
    """
    return [(i, len(i)) for i in lst]
