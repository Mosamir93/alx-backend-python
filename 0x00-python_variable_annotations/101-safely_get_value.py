#!/usr/bin/env python3
"""
This module contains a function that retrieves a value
from a dictionary or returns a default value.
"""
from typing import TypeVar, Mapping, Any, Union
T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any, default: Union[T, None] = None
        ) -> Union[Any, T]:
    """
    Retrieves a value from a dictionary
    or returns a default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
