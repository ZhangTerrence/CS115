#########################################
# Name: Terrence Zhang
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# Homework 2
#########################################
import sys

# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
    [['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10]]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.
from functools import reduce

def letterScore(letter, score_list):
    """Returns scrabble score of a letter"""
    return list(filter(lambda l: l[0] == letter, score_list))[0][1]

def wordScore(S, score_list):
    """Returns scrabble score of a word"""
    return reduce(lambda x, y: x + y, map(lambda x: letterScore(x, score_list), S))

def scoreList(Rack):
    """Returns a list of all words in Dictionary and their scrabble scores that can be made from letter Rack"""
    def check(word, R):
        if word == "":
            return []
        elif word[0] in R:
            index = R.index(word[0])
            return [True] + check(word[1:], R[:index] + R[index+1:])
        return [False]
    sorted_list = list(filter(lambda y: False not in y[0], map(lambda x: [check(x, Rack), x], Dictionary)))
    return list(map(lambda x: [x[-1], wordScore(x[-1], scrabbleScores)], sorted_list))

def bestWord(Rack):
    """Returns the word with the highest score and its score that can be made from letter Rack"""
    return list(reduce(lambda x, y: x if x[-1] > y[-1] else y, scoreList(Rack) + [['', 0]]))
























