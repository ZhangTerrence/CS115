########################################
# Name: Terrence Zhang
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# Lab 10
########################################
import sys
import random

def createOneRow(width):
    """Returns one row of zeros of width "width"  You should use this in your createBoard(width, height) function"""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """Returns a 2d array with "height" rows and "width" cols"""
    A = []
    for row in range(height):
        A += [createOneRow(width)]
    return A

def printBoard(A):
    """Prints the 2d list-of-lists A without spaces (using sys.stdout.write)"""
    for row in A:
        for col in row:
            sys.stdout.write(str(col))
        sys.stdout.write('\n')

def diagonalize(width, height):
    """Creates an empty board and then modifies it so that it has a diagonal strip of "on" cells"""
    A = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def innerCells(w, h):
    """Creates an empty board and then modifies it so that all cells that are not on the border are "on" cells"""
    A = createBoard(w, h)
    for row in range(h):
        for col in range(w):
            if row == 0 or col == 0 or row == h - 1 or col == w - 1:
                A[row][col] = 0
            else:
                A[row][col] = 1
    return A


def randomCells(w, h):
    """Creates an empty board and then modifies it so that all cells that are not on the border are randomly "on" cells"""
    A = createBoard(w, h)
    for row in range(h):
        for col in range(w):
            if row == 0 or col == 0 or row == h - 1 or col == w - 1:
                A[row][col] = 0
            else:
                A[row][col] = random.choice([0, 1])
    return A


def copy(A):
    """Returns a deep copy of A"""
    B = createBoard(len(A[0]), len(A))
    for row in range(len(A)):
        for col in range(len(A[0])):
            B[row][col] = A[row][col]
    return B


def innerReverse(A):
    """Returns a new generation of A that would have the opposite value cells of A's cells except for the outer edges"""
    B = copy(A)
    for row in range(len(B)):
        for col in range(len(B[0])):
            if row == 0 or col == 0 or row == len(B) - 1 or col == len(B[0]) - 1:
                B[row][col] = 0
            else:
                B[row][col] = 1 - B[row][col]
    return B


def next_life_generation(A):
    """Makes a copy of A and then advanced one generation of Conway's game of life within the *inner cells* of that
    copy. The outer edge always stays 0"""
    def countNeighbors(row, col, Array):
        neighbors = 0
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if Array[row + x][col + y] == 1:
                    neighbors += 1
        return neighbors - Array[row][col]
    B = copy(A)

    for row in range(len(B)):
        for col in range(len(B[0])):
            if row == 0 or col == 0 or row == len(B) - 1 or col == len(B[0]) - 1:
                B[row][col] = 0
            else:
                if B[row][col] == 1:
                    if countNeighbors(row, col, A) < 2 or countNeighbors(row, col, A) > 3:
                        B[row][col] = 0
                if B[row][col] == 0 and countNeighbors(row, col, A) == 3:
                    B[row][col] = 1
    return B















