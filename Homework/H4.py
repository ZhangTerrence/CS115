#########################################
# Name: Terrence Zhang
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# Homework 4
#########################################

def addingRow(L):
    """Returns a list of sums of adjacent elements in a list"""
    if len(L) == 1:
        return []
    else:
        return [L[0] + L[1]] + addingRow(L[1:])

def pascal_row(n):
    """Returns a list containing the integers found on the n-th row of Pascal's Triangle"""
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]
    else:
        return [1] + addingRow(pascal_row(n-1)) + [1]

def pascal_triangle(n):
    """Returns a list of lists containing all the integers from the 0th row to the n-th row of Pascal's Triangle"""
    if n < 0:
        return []
    else:
        return pascal_triangle(n-1) + [pascal_row(n)]

def test_pascal_row():
    """Tests the pascal_row function"""
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1, 1]
    assert pascal_row(3) == [1, 3, 3, 1]
    assert pascal_row(5) == [1, 5, 10, 10, 5, 1]

def test_pascal_triangle():
    """Tests the pascal_triangle function"""
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1], [1, 1]]
    assert pascal_triangle(3) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
