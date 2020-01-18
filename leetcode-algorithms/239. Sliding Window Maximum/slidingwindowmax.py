from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        res = []
        candidates = deque()
        for i, n in enumerate(nums):
            while candidates and nums[candidates[-1]] <= n:
                candidates.pop()
            candidates += [i]
            if i - candidates[0] >= k:
                candidates.popleft()
            if i + 1 >= k:
                res.append(nums[candidates[0]])
        return res