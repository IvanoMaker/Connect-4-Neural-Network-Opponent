# Combination class for solving solutions on the gameboard
class Combination:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
    # is_full, returns a boolean value for if a combination is filled with the same pieces
    def is_full(self):
        if (self.p1 == "X" and self.p2 == "X" and self.p3 == "X" and self.p4 == "X"):
            return "X"
        elif (self.p1 == "O" and self.p2 == "O" and self.p3 == "O" and self.p4 == "O"):
            return "O"
        else:
            return "#"
