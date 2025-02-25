# main board class
# used for structure of the game

import copy
from Combination import *

# charMapLst, maps the characters X and O to 1 and -1 for training purposes
# takes a list and performs the mapping on each element in the list
def charMapLst(l):
    r_l = []
    for a in l:
        if a == "X":
            r_l.append(1)
        elif a == "O":
            r_l.append(-1)
        else:
            r_l.append(0)
    return r_l

# Board class definition
class Board:
    def __init__(self):
        self.mtx = [[], [], [], [], [], [], []]
        self.solution_set = []
        for n in self.mtx:
            for _ in range(6):
                n.append(None)

    # laboriously add each solution for a 7x6 gameboard
    def update_solution(self):
        self.solution_set = []
        self.solution_set.append(Combination(self.mtx[0][0], self.mtx[1][1], self.mtx[2][2], self.mtx[3][3]))
        self.solution_set.append(Combination(self.mtx[1][1], self.mtx[2][2], self.mtx[3][3], self.mtx[4][4]))
        self.solution_set.append(Combination(self.mtx[2][2], self.mtx[3][3], self.mtx[4][4], self.mtx[5][5]))
        self.solution_set.append(Combination(self.mtx[1][0], self.mtx[2][1], self.mtx[3][2], self.mtx[4][3]))
        self.solution_set.append(Combination(self.mtx[2][1], self.mtx[3][2], self.mtx[4][3], self.mtx[5][4]))
        self.solution_set.append(Combination(self.mtx[3][2], self.mtx[4][3], self.mtx[5][4], self.mtx[6][5]))
        self.solution_set.append(Combination(self.mtx[0][3], self.mtx[1][2], self.mtx[2][1], self.mtx[3][0]))
        self.solution_set.append(Combination(self.mtx[0][4], self.mtx[1][3], self.mtx[2][2], self.mtx[3][1]))
        self.solution_set.append(Combination(self.mtx[0][5], self.mtx[1][4], self.mtx[2][3], self.mtx[3][2]))
        self.solution_set.append(Combination(self.mtx[1][3], self.mtx[2][2], self.mtx[3][1], self.mtx[4][0]))
        self.solution_set.append(Combination(self.mtx[1][4], self.mtx[2][3], self.mtx[3][2], self.mtx[4][1]))
        self.solution_set.append(Combination(self.mtx[1][5], self.mtx[2][4], self.mtx[3][3], self.mtx[4][2]))
        self.solution_set.append(Combination(self.mtx[2][3], self.mtx[3][2], self.mtx[4][1], self.mtx[5][0]))
        self.solution_set.append(Combination(self.mtx[2][4], self.mtx[3][3], self.mtx[4][2], self.mtx[5][1]))
        self.solution_set.append(Combination(self.mtx[2][5], self.mtx[3][4], self.mtx[4][3], self.mtx[5][2]))
        self.solution_set.append(Combination(self.mtx[3][3], self.mtx[4][2], self.mtx[5][1], self.mtx[6][0]))
        self.solution_set.append(Combination(self.mtx[3][4], self.mtx[4][3], self.mtx[5][2], self.mtx[6][1]))
        self.solution_set.append(Combination(self.mtx[3][5], self.mtx[4][4], self.mtx[5][3], self.mtx[6][2]))

        for a in range(7):
            self.solution_set.append(Combination(self.mtx[a][0], self.mtx[a][1], self.mtx[a][2], self.mtx[a][3]))
            self.solution_set.append(Combination(self.mtx[a][1], self.mtx[a][2], self.mtx[a][3], self.mtx[a][4]))
            self.solution_set.append(Combination(self.mtx[a][2], self.mtx[a][3], self.mtx[a][4], self.mtx[a][5]))
        for b in range(6):
            self.solution_set.append(Combination(self.mtx[0][b], self.mtx[1][b], self.mtx[2][b], self.mtx[3][b]))
            self.solution_set.append(Combination(self.mtx[1][b], self.mtx[2][b], self.mtx[3][b], self.mtx[4][b]))
            self.solution_set.append(Combination(self.mtx[2][b], self.mtx[3][b], self.mtx[4][b], self.mtx[5][b]))
            self.solution_set.append(Combination(self.mtx[3][b], self.mtx[4][b], self.mtx[5][b], self.mtx[6][b]))

    # method for placing a piece, takes the character and the column number (1 INDEXED)
    def place(self, piece, column):
        if self.mtx[column][5] is not None:
            return False
        
        for row in range(6):
            if self.mtx[column][row] is None:
                self.mtx[column][row] = piece
                self.update_solution()
                return True
    
        return False

    # boolean solved function, returns the character who won the game, # if no one has won or the game is tied
    def solved(self):
        for s in self.solution_set:
            if s.is_full() == "O":
                return s.is_full()
            elif s.is_full() == "X":
                return s.is_full()
        return "#"

    # draw, draws the game board in the console
    def draw(self):
        string = ""
        for i in reversed(range(6)):
            for j in range(7):
                if self.mtx[j][i] is None:
                    string += "[ ]"
                else:
                    string += f"[{self.mtx[j][i]}]"
            string += "\n"
        string += "---------------------\n"
        for k in range(7):
            string += f"[{k+1}]"
        string += "\n"
        return string

    # encode, encode the gameboard for training purposes
    # uses the charMapLst function defined above
    def encoded(self):
        mtx = []
        for i in range(7):
            mtx.append(charMapLst(self.mtx[i]))
        flattened_mtx = [item for sublist in mtx for item in sublist]
        return flattened_mtx

    # tie, returns true if the gameboard is full and no one has won
    def tie(self):
        if self.isFull():
            if self.solved() == "#":
                return True
        return False

    # isFull, returns true if the gameboard is full
    def isFull(self):    
        return all(all(cell is not None for cell in row) for row in self.mtx)

    # copy, creates a deep copy of the board
    def copy(self):
        return copy.deepcopy(self)
