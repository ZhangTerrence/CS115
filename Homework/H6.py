#########################################
# Name: Terrence Zhang
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# Homework 6
#########################################
from functools import reduce

def compress(S):
    """Returns the run-length sequence of a string"""
    l = []
    return reduce(lambda x,y: print(x,y),S)
print(compress('0'*64))
print(compress('01'*32))

def uncompress(C):
    pass

def compression(S):
    return len(compress(S))/len(S)