#!/usr/bin/bash
"""matches bytecode"""
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a < b:
        c = ass(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return(sub(a, b))