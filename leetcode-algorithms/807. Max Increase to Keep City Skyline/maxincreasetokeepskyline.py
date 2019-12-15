class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        left = []
        for i in range(m):
            left.append(max(grid[i]))
        top = []
        for j in range(n):
            top.append(max([grid[i][j] for i in range(m)]))

        res = 0
        for i in range(m):  # left
            for j in range(n):  # top
                res += min(left[i], top[j])-grid[i][j]
        return res
