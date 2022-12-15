#########################################
# Name: Terrence Zhang
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# Homework 13
#########################################

class Board:
    def __init__(self, width=7, height=6):
        """Constructor for list"""
        A = []
        for row in range(height+2):
            rowL = []
            if row == height:
                for col in range(width):
                    if col == width-1:
                        rowL += ['---']
                    else:
                        rowL += ['--']
            elif row == height+1:
                for col in range(width):
                    rowL += [' '+str(col)]
            else:
                for col in range(width):
                    if col == width-1:
                        rowL += ['| |']
                    else:
                        rowL += ['| ']
            A += [rowL]
        self.width = width
        self.height = height
        self.A = A

    def __str__(self):
        """Converts list to board string"""
        s = ''
        for row in self.A:
            for col in row:
                s += col
            s += '\n'
        return s

    def __repr__(self):
        """Prints board"""
        return self.__str__()

    def allowMove(self, col):
        """Returns True if player is allowed to move into column. Else returns False"""
        if col in range(self.width):
            L = []
            [L.append(x[col]) for x in self.A]
            if '| ' in L or '| |' in L:
                return True
            else:
                return False
        else:
            return False

    def addMove(self, col, ox):
        """Adds players checker ('X' or 'O') to column"""
        if self.allowMove(col):
            L = []
            [L.append(x[col]) for x in self.A]
            for i in range(0, len(L)):
                if L[::-1][i] == "| " or L[::-1][i] == "| |":
                    self.A[len(L)-i-1][col] = self.A[len(L)-i-1][col][:1] + ox + self.A[len(L)-i-1][col][2:]
                    return
            return
        else:
            return False

    def setBoard(self, move_string):
        """ takes in a string of columns and places
            alternating checkers in those columns,
            starting with 'X'

            For example, call b.setBoard('012345')
            to see 'X's and 'O's alternate on the
            bottom row, or b.setBoard('000000') to
            see them alternate in the left column.

            moveString must be a string of integers
        """
        nextCh = 'X'  # start by playing 'X'
        for colString in move_string:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X':
                nextCh = 'O'
            else:
                nextCh = 'X'

    def winsFor(self, ox):
        """Returns True if given check ('X' or 'O') has won the game. Else return False"""
        allLocations = []
        for row in range(self.height):
            for col in range(self.height):
                if self.A[row][col][1] == ox:
                    allLocations.append((row, col))
        for location in allLocations:
            for i in range(-3, 1):
                horizontal, vertical = 0, 0
                diagNeg, diagPos = 0, 0
                for j in range(0, 4):
                    if (location[0], location[1] + i + j) in allLocations:
                        horizontal += 1
                    if (location[0] + i + j, location[1]) in allLocations:
                        vertical += 1
                    if (location[0] + i + j, location[1] + i + j) in allLocations:
                        diagNeg += 1
                    if (location[0] + i + j, location[1] + -1 * (i + j)) in allLocations:
                        diagPos += 1
                if horizontal >= 4 or vertical >= 4 or diagNeg >= 4 or diagPos >= 4:
                    return True
        return False

    def hostGame(self):
        """Runs a loop allowing user(s) to play game"""
        print("Welcome to Connect Four!")
        print(self.__repr__())
        switch = 0
        L = ['X', 'O']
        running = True
        while running:
            choice = input(f"{L[switch]}'s choice: ")
            if self.addMove(int(choice), L[switch]) == False:
                continue
            if self.winsFor(L[switch]):
                print(f"{L[switch]} wins -- Congratulations!")
                print(self.__repr__())
                running = False
            else:
                print(self.__repr__())
                switch = 1 - switch
