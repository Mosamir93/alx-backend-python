#!/usr/bin/env python3
"""
This module contains a function that returns a list of tuples.
"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    A function that returns a list of tuples.
    """
    return [(i, len(i)) for i in lst]
