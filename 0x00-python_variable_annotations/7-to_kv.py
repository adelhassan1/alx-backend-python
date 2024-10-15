#!/usr/bin/env python3
"""
String and int/float to tuple
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes k and v and returns a tuple.
    """
    return (k, v ** 2)
