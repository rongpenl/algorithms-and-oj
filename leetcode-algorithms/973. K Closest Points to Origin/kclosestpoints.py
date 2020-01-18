class Solution:
    def kClosest(self, points, K):
        return heapq.nsmallest(K, points, lambda (x, y): x * x + y * y)
        