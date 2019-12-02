class Solution:
    def twoSum(self, nums, target):
        d = dict()
        for ind, n in enumerate(nums):
            if str(n) in d:
                return [d[str(n)],ind]
            else:
                d[str(target-n)]=ind