
class Solution:
    def __init__(self):
        self.vDict = None

    def solveSudoku(self, board):
        self.solve(board)

    def solve(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    for p in "123456789":
                        board[i][j] = p
                        if not self.isValid(board, i, j):
                            board[i][j] = "."
                        else:
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = "."
                    return False

        return True

    def isValid(self, board, i, j):
        self.vDict = set()
        for k in range(9):
            if board[i][k] != ".":
                if board[i][k] in self.vDict:
                    return False
                self.vDict.add(board[i][k])
        self.vDict = set()
        for k in range(9):
            if board[k][j] != ".":
                if board[k][j] in self.vDict:
                    return False
                self.vDict.add(board[k][j])
        self.vDict = set()
        i1 = i - i % 3
        j1 = j - j % 3
        for s in range(3):
            for t in range(3):
                if board[i1+s][j1+t] != ".":
                    if board[i1+s][j1+t] in self.vDict:
                        return False
                    self.vDict.add(board[i1+s][j1+t])
        return True
