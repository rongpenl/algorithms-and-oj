class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool

        1. Start from lower left corner, search to right to increase,
        2. if exceed, every element to the right discarded,
        3. search the row above, every element on the left are certain to be smaller.
        """
        j = 0
        for row in reversed(matrix):
            while j < len(row) and row[j] < target:
                j += 1
            if j < len(row) and row[j] == target:
                return True
        return False
