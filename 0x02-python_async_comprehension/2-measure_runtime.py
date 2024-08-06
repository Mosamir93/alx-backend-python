#!/usr/bin/env python3
"""This module Imports async_comprehension from the previous
file and write a measure_runtime coroutine that will execute
async_comprehension four times in parallel using asyncio.gather
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel using asyncio.gather.
    Measures the total runtime and returns it.
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    runtime = time.time() - start
    return runtime
