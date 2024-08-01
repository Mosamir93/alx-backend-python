#!/usr/bin/env python3
"""
This module contains a function that returns
the first element of a sequence or None.
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Takes a sequence and returns the first
    element if it exists, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
