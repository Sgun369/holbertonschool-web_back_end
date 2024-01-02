#!/usr/bin/env python
"""Basic annotations - floor"""
import math


def floor(n: float) -> int:
    """ returns the floor of the float."""
    if isinstance(n, float):
        n = math.floor(n)
    return n
