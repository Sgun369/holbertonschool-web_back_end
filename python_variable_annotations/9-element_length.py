#!/usr/bin/env python3
"""Let's duck type an iterable object"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Takes a list of string and returns a list of tuples
    where each tuple contains an element
    from the input list and its corresponding length
    """
    return [(i, len(i)) for i in lst]
