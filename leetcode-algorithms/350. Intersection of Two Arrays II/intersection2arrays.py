from collections import Counter
class Solution:
    def intersect(self, nums1, nums2):
        c1, c2 = Counter(nums1), Counter(nums2)
        res = []
        for key in c1:
            if key in c2:
                res += [key for _ in range(min(c1[key],c2[key]))]
        return res