class Solution:
    def threeSum(self, nums):
        res = set()
        L = len(nums)
        if L < 3:
            return []
        nums.sort()
        for l in range(0, L-2):
            m, r = l+1, L-1
            while m < r:
                if nums[l] + nums[m] + nums[r] == 0:
                    res.add((nums[l], nums[m], nums[r]))
                    m += 1
                    r -= 1
                elif nums[l] + nums[m] + nums[r] < 0:
                    m += 1
                else:
                    r -= 1
        print(res)
        return [list(ele) for ele in res]
