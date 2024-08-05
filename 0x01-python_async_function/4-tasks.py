#!/usr/bin/env python3
"""This module contains an altered wait_n function."""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
