class Solution:
    def __init__(self):
        self.s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

    def numMagicSquaresInside(self, grid):
        res = 0
        m = len(grid)
        if m == 0:
            return res
        n = len(grid[0])
        if n == 0:
            return res
        for i in range(1, m-1):
            for j in range(1, n-1):
                if self.valid(grid, i, j):
                    res += 1
        return res

    def valid(self, grid, i, j):
        if set([grid[i+t][j+s] for s in [-1, 0, 1] for t in [-1, 0, 1]]) != self.s:
            return False
        if grid[i][j] != 5:
            return False
        for t in [-1, 0, 1]:
            if grid[i+t][j-1] + grid[i+t][j] + grid[i+t][j+1] != 15:
                return False
            if grid[i-1][j+t] + grid[i][j+t] + grid[i+1][j+t] != 15:
                return False
        if grid[i-1][j-1] + grid[i+1][j+1] != 10:
            return False
        if grid[i-1][j+1] + grid[i+1][j-1] != 10:
            return False
        return True
