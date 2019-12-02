class Solution:
    def search(self, nums, target, start=None, end=None):
        # print(start, end, nums[start:end])
        if start == None:
            start = 0
            end = len(nums)
        # evaluate base case
        if end-start <= 2:
            for i in range(start, end):
                if nums[i] == target:
                    return i
            return -1
        # recursive case
        mid = (end+start)//2
        if nums[start] <= target <= nums[mid-1]:
            return self.search(nums, target, start, mid)
        if nums[mid] <= target <= nums[end-1]:
            return self.search(nums, target, mid, end)
        else:
            # search in the dis ordered range
            if nums[start] > nums[mid-1]:
                return self.search(nums, target, start, mid)
            elif nums[mid] > nums[end-1]:
                return self.search(nums, target, mid, end)
            else:
                return -1
