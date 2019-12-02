class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        nextAvail = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[nextAvail-1]:
                i += 1
            else:
                nums[nextAvail] = nums[i]
                nextAvail += 1
                continue
        return nextAvail
