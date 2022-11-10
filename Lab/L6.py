###########################################
# Name: Terrence Zhang
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# Lab 6
###########################################

def isOdd(n):
    """Returns whether the integer argument is odd"""
    return n % 2 == 1

def numToBinary(n):
    """Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned"""
    if n == 0:
        return ''
    return numToBinary(n // 2) + str(n % 2)

def binaryToNum(s):
    """Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0"""
    if s == "":
        return 0
    return int(s[-1]) + 2 * binaryToNum(s[:-1])

def increment(s):
    """Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1"""
    result = numToBinary(binaryToNum(s) + 1)
    if len(result) > 8:
        return "0" * 8
    return "0" * (8 - len(result)) + result

def count(s, n):
    """Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors"""
    if n == -1:
        return ''
    print(s)
    count(increment(s), n - 1)

def numToTernary(n):
    """Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned"""
    if n == 0:
        return ""
    return numToTernary(n // 3) + str(n % 3)

def ternaryToNum(s):
    """Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0"""
    if s == "":
        return 0
    return int(s[-1]) + 3 * ternaryToNum(s[:-1])
