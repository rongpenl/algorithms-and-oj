class Solution:

    def helper(self, height):
        if len(height) == 0 or max(height) == 0:
            return 0
        for i in range(len(height)):
            if height[i] > 0:
                break
        j = i+1
        res = 0
        while j < len(height):
            while j < len(height) and height[j] < height[i]:
                j += 1
            res += height[i]*(j-i) - sum(height[i:j])
            # print(i,j,height[i],height[j],res)
            i = j
            j = i+1
        return res

    def trap(self, height):
        if len(height) == 0 or max(height) == 0:
            return 0
        maxInd = height.index(max(height))
        return self.helper(height[:maxInd+1]) + self.helper(list(reversed(height[maxInd:])))
