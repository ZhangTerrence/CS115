#########################################
# Name: Terrence Zhang
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# Homework 6
#########################################
from functools import reduce

# CBS = COMPRESSED_BLOCK_SIZE
CBS = 5

def numToBinary(n):
    """Precondition: integer argument is non-negative. Returns the string with the binary representation of
    non-negative integer n. If n is 0, the empty string is returned"""
    if n == 0:
        return ''
    return numToBinary(n // 2) + str(n%2)

def binaryToNum(s):
    """Precondition: s is a string of 0s and 1s. Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0"""
    if s == "":
        return 0
    return int(s[-1]) + 2 * binaryToNum(s[:-1])

# CBN = COMPRESSED_BLOCK_NUMBER
CBN = binaryToNum('1'*CBS)

def compress(S):
    """Returns the run-length sequence of a string"""
    def encode(string, L):
        if len(string) == 0:
            return L
        elif string[0] == L[-1][0]:
            newL = L
            newL[-1][-1] += 1
            return encode(string[1:], newL)
        else:
            newL = L
            newL[len(newL):] = [[str(1-int(L[-1][0])), 1]]
            return encode(string[1:], newL)
    distributedL =  list(map(lambda x: ([CBN]+[0])*(x[1]//CBN) + [x[1]%CBN] if x[1] > CBN else [x[1]], encode(S, [['0', 0]])))
    binaryL = list(map(lambda x: '0'*(CBS-len(numToBinary(x))) + numToBinary(x), list(reduce(lambda x,y: x+y, distributedL))))
    return reduce(lambda x,y: x+y, binaryL)

def uncompress(C):
    """Reverses the run-length sequence of a string"""
    def decode(string, r):
        if len(string) == 0:
            return ''
        else:
            fill = r * binaryToNum(string[:CBS])
            return fill + decode(string[CBS:], str(1 - int(r)))
    return decode(C, '0')

def compression(S):
    """Returns the ratio between the length of the run-length sequence of a string and its original length"""
    return len(compress(S))/len(S)

def test_compress():
    """Tests the compress functions"""
    MAX_RUN_LENGTH = 2 ** CBS - 1
    assert compress('0' * 64) == '1111100000111110000000010'
    assert compress('01'* 32) == '0000100001000010000100001000010000100001000010000100001000010000100001000010000100' \
                               '0010000100001000010000100001000010000100001000010000100001000010000100001000010000' \
                               '1000010000100001000010000100001000010000100001000010000100001000010000100001000010' \
                               '00010000100001000010000100001000010000100001000010000100001000010000100001'
    assert compress('10' * 32) == '0000000001000010000100001000010000100001000010000100001000010000100001000010000100' \
                                '0010000100001000010000100001000010000100001000010000100001000010000100001000010000' \
                                '1000010000100001000010000100001000010000100001000010000100001000010000100001000010' \
                                '0001000010000100001000010000100001000010000100001000010000100001000010000100001'
    assert compress('0' * MAX_RUN_LENGTH + '1' * MAX_RUN_LENGTH + '0' * (64 - 2 * MAX_RUN_LENGTH)) == '111111111100010'
    assert compress('0' * (MAX_RUN_LENGTH + 1) + '1' * (MAX_RUN_LENGTH + 1) + '0' * (64 - 2 * MAX_RUN_LENGTH - 2)) == \
           '111110000000001111110000000001'
    assert compress('1' * MAX_RUN_LENGTH + '0' * MAX_RUN_LENGTH + '1' * (64 - 2 * MAX_RUN_LENGTH)) == '00000111111111100010'

def test_uncompress():
    """Tests the uncompress function"""
    MAX_RUN_LENGTH = 2 ** CBS - 1
    assert uncompress(compress('0' * 64)) == '0' * 64
    assert uncompress(compress('01'* 32)) == '01'* 32
    assert uncompress(compress('10' * 32)) == '10' * 32
    assert uncompress(compress('0' * MAX_RUN_LENGTH + '1' * MAX_RUN_LENGTH + '0' * (64 - 2 * MAX_RUN_LENGTH))) == \
           '0' * MAX_RUN_LENGTH + '1' * MAX_RUN_LENGTH + '0' * (64 - 2 * MAX_RUN_LENGTH)
    assert uncompress(compress('0' * (MAX_RUN_LENGTH + 1) + '1' * (MAX_RUN_LENGTH + 1) + '0' * (64 - 2 * MAX_RUN_LENGTH - 2))) == \
           '0' * (MAX_RUN_LENGTH + 1) + '1' * (MAX_RUN_LENGTH + 1) + '0' * (64 - 2 * MAX_RUN_LENGTH - 2)
    assert uncompress(compress('1' * MAX_RUN_LENGTH + '0' * MAX_RUN_LENGTH + '1' * (64 - 2 * MAX_RUN_LENGTH))) == \
           '1' * MAX_RUN_LENGTH + '0' * MAX_RUN_LENGTH + '1' * (64 - 2 * MAX_RUN_LENGTH)

def test_compression():
    """Tests the compression function"""
    MAX_RUN_LENGTH = 2 ** CBS - 1
    assert compression('0' * 64) == 0.390625
    assert compression('01' * 32) == 5.0
    assert compression('10' * 32) == 5.078125
    assert compression('0' * MAX_RUN_LENGTH + '1' * MAX_RUN_LENGTH + '0' * (64 - 2 * MAX_RUN_LENGTH)) == 0.234375
    assert compression('0' * (MAX_RUN_LENGTH + 1) + '1' * (MAX_RUN_LENGTH + 1) + '0' * (64 - 2 * MAX_RUN_LENGTH - 2)) == 0.46875
    assert compression('1' * MAX_RUN_LENGTH + '0' * MAX_RUN_LENGTH + '1' * (64 - 2 * MAX_RUN_LENGTH)) == 0.3125