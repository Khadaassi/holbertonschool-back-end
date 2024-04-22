#!/usr/bin/python3

def sum_mixed_list(input_list):
    sum = 0
    for i in input_list:
        if isinstance(i, int):
            sum += i
    return sum
