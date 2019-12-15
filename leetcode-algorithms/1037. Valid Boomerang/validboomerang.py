class Solution:
    def isBoomerang(self, points):
        if points[0] == points[1] or points[0] == points[2] or points[1] == points[2]:
            return False
        else:
            v1 = (points[2][1] - points[0][1], points[2][0] - points[0][0])
            v2 = (points[1][1] - points[0][1], points[1][0] - points[0][0])
            cos = (v1[0]*v2[0] + v1[1]*v2[1])**2 / \
                (v1[0]**2+v1[1]**2)/(v2[0]**2+v2[1]**2)
            if abs(cos-1) < 1e-9:
                return False
            return True
