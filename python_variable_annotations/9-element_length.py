#!/usr/bin/python3

from typing import List, Tuple

def element_length(L: List[str]) -> List[Tuple[str, int]]:
    return [(i, len(i)) for i in L]
