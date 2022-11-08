#########################################
# Name: Terrence Zhang
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# Homework 1
#########################################
from functools import reduce


def multiply(x, y):
    """Returns product of x and y"""
    return x*y


def factorial(n):
    """Returns factorial of n"""
    return reduce(multiply, range(1, n+1))


def add(x, y):
    """Returns sum of x and y"""
    return x+y


def mean(L):
    """Returns mean of a list of integers"""
    return reduce(add, L)/len(L)