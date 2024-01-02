#!/usr/bin/env python3
"""Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable:
    """returns a function that multiplies a float by multiplier"""
    def multiply(num: float) -> float:
        return num * multiplier
    return multiply
