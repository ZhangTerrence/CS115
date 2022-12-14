############################################################
# Name: Terrence Zhang
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# Lab 1
############################################################
from math import factorial
from functools import reduce

def add(x, y):
    """Returns sum of x and y"""
    return x + y

def inverse(x):
    """Returns inverse of x"""
    return 1 / x

def e(n):
    """Returns the sum of the inverses of all factorials up to n"""
    return reduce(add, list(map(inverse, map(factorial, range(n + 1)))))


