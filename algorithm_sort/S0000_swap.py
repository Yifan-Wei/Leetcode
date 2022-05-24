from typing import List
def swap(a, b):
    return b, a

def swap_tmp(a, b):
    tmp = b
    b = a
    a = tmp
    return a, b

def swap_add(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

def swap_xor(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b