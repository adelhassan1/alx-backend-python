#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""


import asyncio
import time
from typing import Gererator
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> Generator[float, None, None]:
    """
    Executes async_comprehension four times in parallel using asyncio.gather.
    """
    s = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    elapsed = time.perf_counter() - s
    return elapsed
