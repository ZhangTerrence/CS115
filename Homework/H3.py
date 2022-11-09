#########################################
# Name: Terrence Zhang
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# Homework 3
#########################################
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


# your code goes here


def giveChange(amount, coins):
    """Given a specific amount and list of possible coins, returns the
    minimum amount of coins needed to make up that amount and also shows
    the combination of coins needed for that amount"""
    if amount == 0:
        return [0, []]
    elif coins == [] and amount > 0:
        return [float("inf"), []]
    elif coins[-1] > amount:
        return giveChange(amount, coins[:-1])
    elif amount < 0:
        return giveChange(amount + coins[-1], coins[:-1])
    else:
        use = giveChange(amount - coins[-1], coins)
        lose = giveChange(amount, coins[:-1])
        if use[0] + 1 < lose[0]:
            return [use[0] + 1, [coins[-1]] + use[1]]
        return lose


# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
    [['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10]]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from functools import reduce


def wordsWithScore(dct, scores):
    """List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    """
    def findScore(word, score_list):
        return reduce(lambda x, y: x + y, map(lambda letter: list(filter(lambda l: l[0] == letter, score_list))[0][1], word))
    return list(map(lambda z: [z, findScore(z, scores)], dct))
    # One line
    # return reduce(lambda z, y: z+y, map(lambda x: [[x, reduce(lambda v, w: v+w, map(lambda u: list(filter(lambda l: l[0] == u, scores))[0][1], x))]], dct))


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
' (Notice that you cannot assume anything about the length of the list.)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def take(n, L):
    """Returns the list L[0:n], assuming L is a list and n is at least 0."""
    if n == 0 or L == []:
        return []
    else:
        return [L[0]] + take(n - 1, L[1:])


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def drop(n, L):
    """Returns the list L[n:], assuming L is a list and n is at least 0."""
    if n == 0:
        return L
    else:
        return drop(n - 1, L[1:])
