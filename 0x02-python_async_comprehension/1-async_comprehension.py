#!/usr/bin/env python3
"""This module Imports async_generator from the previous task and then
write a coroutine called async_comprehension that takes no arguments."""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers.
    """
    return [i async for i in async_generator()]
