#!/usr/bin/python3

def make_multiplier(multiplier: float) -> callable:
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
