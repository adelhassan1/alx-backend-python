#!/usr/bin/env python3
"""
Multiplier
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float and returns a function that multiplies a float by multiplier.
    """
    def multiplier_function(value: float) -> float:
        """
        Takes a value and returns it multiplied with the multipler.
        """
        return value * multiplier
    return multiplier_function
