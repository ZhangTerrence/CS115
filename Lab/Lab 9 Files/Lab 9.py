########################################
# Name: Terrence Zhang
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# Lab 9
########################################
from cs5png import *

def mult(c, n):
    """Return product of c and n using loop"""
    result = 0
    for i in range(n):
        result += c
    return result

def update(c, n):
    """Returns z after running z = z**2 + c n times"""
    z = 0
    for i in range(n):
        z = z ** 2 + c
    return z


def inMSet(c, n):
    """Returns whether c is in Mandelbrot set. False if abs(z) > 2"""
    z = 0
    for i in range(n):
        z = z ** 2 + c
        if abs(z) > 2:
            return False
    return True

def weWantThisPixel(col, row):
    """ a function that returns True if we want
        the pixel at col, row and False otherwise
    """
    if col % 10 == 0 or row % 10 == 0:
        return True
    return False

def test():
    """Example function showing how to create an image"""
    width = 300
    height = 200
    image = PNGImage(width, height)

    for col in range(width):
        for row in range(height):
            if weWantThisPixel(col, row) == True:
                image.plotPoint(col, row)
    image.saveFile()

def scale(pix, pixelMax, floatMin, floatMax):
    """Parameters:
        pix, the CURRENT pixel column (or row)
        pixMax, the total # of pixel columns
        floatMin, the min floating-point value
        floatMax, the max floating-point value
    Returns the floating-point value that corresponds to pix"""
    return floatMin + ((abs(floatMin) + abs(floatMax)) * pix / pixelMax)

def mset(width, height, n):
    """Creates an image of the Mandelbrot set"""
    image = PNGImage(width, height)

    for col in range(width):
        for row in range(height):
            x = scale(col, width, -2.0, 1.0)
            y = scale(row, height, -1.0, 1.0)
            c = x + y * 1j
            if inMSet(c, n) == True:
                image.plotPoint(col, row)
    image.saveFile()
















