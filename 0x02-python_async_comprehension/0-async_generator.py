#!/usr/bin/env python3
"""This module contains a coroutine called
async_generator that takes no arguments."""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously generates random numbers.
    Loops 10 times, each time asynchronously waits
    1 second, then yields a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
