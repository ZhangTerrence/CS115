#########################################
# Name: Terrence Zhang
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# Homework 6
#########################################
from functools import reduce

# CBS = COMPRESSED_BLOCK_SIZE
CBS = 5

def numToBinary(n):
    """Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned."""
    if n == 0:
        return ''
    return numToBinary(n // 2) + str(n%2)

def binaryToNum(s):
    """Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0."""
    if s == "":
        return 0
    return int(s[-1]) + 2 * binaryToNum(s[:-1])

# CBN = COMPRESSED_BLOCK_NUMBER
CBN = binaryToNum('1'*CBS)

def compress(S):
    """Returns the run-length sequence of a string"""
    def split(string, L):
        if len(string) == 0:
            return L
        elif string[0] == L[-1][0]:
            newL = L
            newL[-1][-1] += 1
            return split(string[1:], newL)
        else:
            newL = L
            newL[len(newL):] = [[str(1-int(L[-1][0])), 1]]
            return split(string[1:], newL)
    L1 =  list(map(lambda x: ([CBN]+[0])*(x[1]//CBN) + [x[1]%CBN] if x[1] > CBN else [x[1]], split(S, [['0', 0]])))
    L2 = list(map(lambda x: '0'*(CBS-len(numToBinary(x))) + numToBinary(x), list(reduce(lambda x,y: x+y, L1))))
    return reduce(lambda x,y: x+y, L2)

def uncompress(C):
    """Reverses the run-length sequence of a string"""
    pass

def compression(S):
    return len(compress(S))/len(S)