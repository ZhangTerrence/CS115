###########################################
# Name: Terrence Zhang
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# Lab 2
###########################################

def dot(L, K):
    """Returns dot product of L and K"""
    if L == [] and K == []:
        return 0.0
    return L[0] * K[0] + dot(L[1:], K[1:])

def explode(S):
    """Imitates list function"""
    if S == "":
        return []
    return [S[0]] + explode(S[1:])

def ind(e, L):
    """Imitates index function"""
    if L == [] or L == '' or L[0] == e:
        return 0
    return 1 + ind(e, L[1:])

def removeAll(e, L):
    """Returns new list where all incidents of e in L are removed. Only looks at top-level of L"""
    if L == []:
        return []
    elif L[0] == e:
        return removeAll(e, L[1:])
    return [L[0]] + removeAll(e, L[1:])

def myFilter(f, L):
    """Imitates filter function"""
    if L == []:
        return []
    else:
        if f(L[0]):
            return [L[0]] + myFilter(f, L[1:])
        return myFilter(f, L[1:])

def deepReverse(L):
    """Returns deep-level reverse of L"""
    if L == []:
        return []
    else:
        if isinstance(L[-1], list):
            return [deepReverse(L[-1])] + deepReverse(L[:-1])
        return [L[-1]] + deepReverse(L[:-1])