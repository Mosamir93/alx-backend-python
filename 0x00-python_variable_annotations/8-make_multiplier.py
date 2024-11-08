#!/usr/bin/env python3
"""
This module takes a float as argument and returns a
function that multiplies a float by the argument.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    A type-annotated function make_multiplier that takes a float multiplier as
    argument and returns a function that multiplies a float by multiplier.
    """
    def multiplier_function(n: float) -> float:
        return n * multiplier

    return multiplier_function
